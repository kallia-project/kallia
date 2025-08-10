# Document Q&A

Build a document question-answering system using Kallia with LangChain integration.

## Quick Start with Playground

1. Start the playground:

   ```bash
   cd kallia/playground
   docker-compose up -d
   ```

2. Open `http://localhost:8000`
3. Upload a PDF file
4. Ask questions about the document

## LangChain Integration

### Setup

```python
from langchain_core.documents import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import requests

# Initialize LangChain components
embeddings = OpenAIEmbeddings()
llm = OpenAI(temperature=0.7)
```

### Process Document with Kallia

```python
def process_document_with_kallia(file_path):
    """Process document using Kallia API"""

    response = requests.post(
        "http://localhost:8000/documents",
        json={
            "url": file_path,
            "page_number": 1,
            "temperature": 0.7,
            "max_tokens": 4000
        }
    )

    chunks = response.json()["documents"][0]["chunks"]

    # Convert to LangChain documents
    documents = []
    for i, chunk in enumerate(chunks):
        doc = Document(
            page_content=chunk["original_text"],
            metadata={
                "summary": chunk["concise_summary"],
                "question": chunk["question"],
                "answer": chunk["answer"],
                "chunk_id": i
            }
        )
        documents.append(doc)

    return documents
```

### Create Vector Store

```python
def create_qa_system(documents):
    """Create QA system with vector store"""

    # Create vector store from documents
    vectorstore = FAISS.from_documents(documents, embeddings)

    # Create retrieval QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )

    return qa_chain
```

### Complete Example

```python
import requests
from langchain_core.documents import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

class KalliaLangChainQA:
    def __init__(self, openai_api_key):
        self.embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        self.llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        self.qa_chain = None

    def load_document(self, file_path):
        """Load and process document with Kallia"""

        # Process with Kallia
        response = requests.post(
            "http://localhost:8000/documents",
            json={
                "url": file_path,
                "page_number": 1,
                "temperature": 0.7,
                "max_tokens": 4000
            }
        )

        chunks = response.json()["documents"][0]["chunks"]

        # Convert to LangChain documents
        documents = []
        for i, chunk in enumerate(chunks):
            doc = Document(
                page_content=chunk["original_text"],
                metadata={
                    "summary": chunk["concise_summary"],
                    "question": chunk["question"],
                    "answer": chunk["answer"],
                    "chunk_id": i,
                    "source": file_path
                }
            )
            documents.append(doc)

        # Create vector store and QA chain
        vectorstore = FAISS.from_documents(documents, self.embeddings)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True
        )

        return len(documents)

    def ask_question(self, question):
        """Ask a question about the loaded document"""

        if not self.qa_chain:
            raise ValueError("No document loaded. Call load_document() first.")

        result = self.qa_chain({"query": question})

        return {
            "answer": result["result"],
            "sources": [
                {
                    "content": doc.page_content[:200] + "...",
                    "summary": doc.metadata.get("summary", ""),
                    "chunk_id": doc.metadata.get("chunk_id", "")
                }
                for doc in result["source_documents"]
            ]
        }

# Usage
qa_system = KalliaLangChainQA(openai_api_key="your-api-key")

# Load document
num_chunks = qa_system.load_document("research_paper.pdf")
print(f"Loaded {num_chunks} chunks")

# Ask questions
answer = qa_system.ask_question("What is the main topic of this paper?")
print(f"Answer: {answer['answer']}")
print(f"Sources: {len(answer['sources'])} chunks")
```

## Best Practices

- **Chunk Quality**: Kallia's semantic chunks work better than fixed-size chunks
- **Retrieval**: Use 3-5 chunks for context without overwhelming the LLM
- **Memory**: Implement conversation memory for follow-up questions
- **Error Handling**: Handle API errors and empty results gracefully

## Next Steps

- Try [Form Filling](form-filling.md) for structured data extraction
- Check [REST API](../fundamentals/rest-api.md) for more endpoints
- Learn about [Docker setup](../fundamentals/docker.md) for deployment
