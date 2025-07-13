import constants as Constants
import settings as Settings
from uuid import uuid4
from typing import Any, Dict, List, TypedDict
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langgraph.graph import START, StateGraph


class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


class QA:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name=Constants.EMBEDDINGS_MODEL_NAME
        )
        self.vector_store = InMemoryVectorStore(self.embeddings)
        self.prompt: PromptTemplate = hub.pull(Constants.RAG_PROMPT)
        self.llm = ChatOpenAI(
            api_key=Settings.KALLIA_PROVIDER_API_KEY,
            base_url=Settings.KALLIA_PROVIDER_BASE_URL,
            model=Settings.KALLIA_PROVIDER_MODEL,
        )

    def add_documents(self, documents: List[Document]) -> None:
        uuids = [str(uuid4()) for _ in range(len(documents))]
        self.vector_store.add_documents(documents=documents, ids=uuids)

    def retrieve(self, state: State) -> Dict[str, List[Document]]:
        retrieved_docs = self.vector_store.similarity_search(state["question"])
        return {"context": retrieved_docs}

    def generate(self, state: State) -> Dict[str, str]:
        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = self.prompt.invoke(
            {"question": state["question"], "context": docs_content}
        )
        response = self.llm.invoke(messages)
        return {"answer": response.content}

    def build(self, message: str) -> Dict[str, Any]:
        graph_builder = StateGraph(State).add_sequence([self.retrieve, self.generate])
        graph_builder.add_edge(START, "retrieve")
        graph = graph_builder.compile()
        return graph.invoke({"question": message})
