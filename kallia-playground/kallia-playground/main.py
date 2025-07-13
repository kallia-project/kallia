import json
import chainlit as cl
from typing import List
from chainlit import make_async
from kallia.chunker import Chunker
from kallia.documents import Documents
from qa import QA
from pdfminer.pdfinterp import resolve1
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from langchain_core.documents import Document


def get_page_count(source: str) -> int:
    with open(source, "rb") as f:
        parser = PDFParser(f)
        document = PDFDocument(parser)
        return resolve1(document.catalog["Pages"])["Count"]


def add_documents(source: str, page_number: int) -> None:
    documents = []

    markdown = Documents.to_markdown(source, page_number, 0.0, 8192)
    chunks = Chunker.create(markdown, 0.0, 8192)

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

    page_count = get_page_count(file.path)

    for n in range(1, page_count + 1):
        await make_async(add_documents)(file.path, n)

        msg.content = f"Processing document `{n}/{page_count}`..."
        await msg.update()

    msg.content = f"Processing `{file.name}` done. You can now ask questions!"
    await msg.update()


@cl.on_message
async def on_message(message: cl.Message):
    qa: QA = cl.user_session.get("qa")

    res = qa.build(message.content)

    answer = res["answer"]
    source_documents: List[Document] = res["context"]

    text_elements: List[cl.Text] = []

    if source_documents:
        for source_idx, source_doc in enumerate(source_documents):
            source_name = f"source_{source_idx}"
            text_elements.append(
                cl.Text(
                    content=source_doc.page_content, name=source_name, display="side"
                )
            )
        source_names = [e.name for e in text_elements]

        if source_names:
            answer += f"\nSources: {', '.join(source_names)}"
        else:
            answer += "\nNo sources found"

    await cl.Message(content=answer, elements=text_elements).send()
