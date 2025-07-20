import constants as Constants
import settings as Settings
import prompts as Prompts
from uuid import uuid4
from typing import Any, Dict, List
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings


class QA:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name=Constants.EMBEDDINGS_MODEL_NAME
        )
        self.vector_store = InMemoryVectorStore(self.embeddings)
        self.llm = ChatOpenAI(
            api_key=Settings.KALLIA_PROVIDER_API_KEY,
            base_url=Settings.KALLIA_PROVIDER_BASE_URL,
            model=Settings.KALLIA_PROVIDER_MODEL,
        )

    def add_documents(self, documents: List[Document]) -> None:
        uuids = [str(uuid4()) for _ in range(len(documents))]
        self.vector_store.add_documents(documents=documents, ids=uuids)

    def invoke(
        self, question: str, histories: List[Dict[str, str]], memories: str
    ) -> Dict[str, Any]:
        documents = self.vector_store.similarity_search(question)
        context = "\n\n".join(doc.page_content for doc in documents)
        conversation = ""
        for history in histories:
            conversation += (
                f"<{history['role']}>{history['content']}</{history['role']}>"
            )
        user_message = f"<memories>{memories}</memories><context>{context}</context><histories>{conversation}</histories><question>{question}</question>"
        messages = [
            {"role": "system", "content": Prompts.QA_PROMPT},
            {"role": "user", "content": user_message},
        ]
        answer = self.llm.invoke(messages)
        return {"documents": documents, "answer": answer.content}
