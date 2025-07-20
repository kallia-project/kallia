import json
import logging
import chainlit as cl
import constants as Constants
import kallia_core.models as Models
from typing import List
from chainlit import make_async
from kallia_core.logger import Logger
from kallia_core.chunker import Chunker
from kallia_core.documents import Documents
from kallia_core.memories import Memories
from qa import QA
from pdfminer.pdfinterp import resolve1
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from langchain_core.documents import Document

logger = logging.getLogger(__name__)
Logger.config(logger)


def get_page_count(source: str) -> int:
    with open(source, "rb") as f:
        parser = PDFParser(f)
        document = PDFDocument(parser)
        return resolve1(document.catalog["Pages"])["Count"]


def add_documents(source: str, page_number: int) -> None:
    documents = []

    markdown = Documents.to_markdown(source, page_number)
    chunks = Chunker.create(markdown)

    for chunk in chunks:
        doc = Document(
            page_content=json.dumps(chunk, ensure_ascii=False),
            metadata={"page_number": page_number, "source": source},
        )
        documents.append(doc)

    qa: QA = cl.user_session.get("qa")
    qa.add_documents(documents)


@cl.on_chat_start
async def on_chat_start():
    files = None

    while files is None:
        files = await cl.AskFileMessage(
            content="Please upload a `PDF` file to begin!",
            accept=["application/pdf"],
            max_size_mb=20,
            timeout=180,
        ).send()

    file = files[0]

    msg = cl.Message(content=f"Processing `{file.name}`...")
    await msg.send()

    qa = await make_async(QA)()

    cl.user_session.set("qa", qa)
    cl.user_session.set("histories", [])

    page_count = get_page_count(file.path)

    try:
        for n in range(1, page_count + 1):
            await make_async(add_documents)(file.path, n)

            msg.content = f"Processing document `{n}/{page_count}`..."
            await msg.update()

        msg.content = f"Processing `{file.name}` done. You can now ask questions!"
        await msg.update()
    except Exception as e:
        logger.error(f"Internal Server Error {e}")
        await cl.context.emitter.send_toast(
            message="Internal Server Error", type="error"
        )


@cl.on_message
async def on_message(message: cl.Message):
    msg = cl.Message(content="Loading...")
    await msg.send()

    qa: QA = cl.user_session.get("qa")
    histories: List = cl.user_session.get("histories")

    long_term_memory_histories = histories
    short_term_memory_histories = histories

    if len(histories) > Constants.LONG_TERM_MEMORY_MAX_HISTORIES:
        long_term_memory_histories = histories[
            -Constants.LONG_TERM_MEMORY_MAX_HISTORIES :
        ]

    if len(histories) > Constants.SHORT_TERM_MEMORY_MAX_HISTORIES:
        short_term_memory_histories = histories[
            -Constants.SHORT_TERM_MEMORY_MAX_HISTORIES :
        ]

    try:
        memories = Memories.create(
            [Models.Message(**history) for history in long_term_memory_histories]
        )
        results = await make_async(qa.invoke)(
            message.content, short_term_memory_histories, memories
        )
    except Exception as e:
        logger.error(f"Internal Server Error {e}")
        await cl.context.emitter.send_toast(
            message="Internal Server Error", type="error"
        )
        return

    answer = results["answer"]
    histories.extend(
        [
            {"role": "user", "content": message.content},
            {"role": "assistant", "content": answer},
        ]
    )
    cl.user_session.set("histories", histories)

    elements: List[cl.Text] = []
    documents: List[Document] = results["documents"]

    if documents:
        for i, doc in enumerate(documents):
            source_name = f"source_{i}"
            elements.append(
                cl.Text(content=doc.page_content, name=source_name, display="side")
            )
        source_names = [e.name for e in elements]

        if source_names:
            answer += f"\nSources: {', '.join(source_names)}"
        else:
            answer += "\nNo sources found"

    memory_element = cl.Text(
        content=json.dumps(memories, ensure_ascii=False),
        name="memory",
        display="side",
    )
    elements.append(memory_element)

    msg.content = f"{answer} Memory: memory"
    msg.elements = elements

    await msg.update()
