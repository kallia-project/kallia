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

## Vector Database Integration

### Simple Setup

```python
import requests
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.documents import Document

# Initialize embeddings
embeddings = OpenAIEmbeddings(api_key="your-openai-key")
```

### Process and Store Documents

```python
def create_vector_store(file_path):
    # Get chunks from Kallia
    response = requests.post("http://localhost:8000/documents", json={
        "url": file_path
    })
    chunks = response.json()["documents"][0]["chunks"]

    # Convert to documents
    documents = [
        Document(
            page_content=chunk["original_text"],
            metadata={"summary": chunk["concise_summary"]}
        )
        for chunk in chunks
    ]

    # Create vector store
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore
```

### Ask Questions

```python
def ask_question(vectorstore, question):
    # Find similar chunks
    docs = vectorstore.similarity_search(question, k=3)

    # Combine relevant content
    context = "\n".join([doc.page_content for doc in docs])

    # You can use any LLM here to generate answer from context
    return {
        "context": context,
        "sources": [doc.metadata.get("summary", "") for doc in docs]
    }
```

### Complete Example

```python
import requests
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.documents import Document

class SimpleQA:
    def __init__(self, openai_key):
        self.embeddings = OpenAIEmbeddings(api_key=openai_key)
        self.vectorstore = None

    def load_document(self, file_path):
        # Process with Kallia
        response = requests.post("http://localhost:8000/documents", json={
            "url": file_path
        })
        chunks = response.json()["documents"][0]["chunks"]

        # Create documents
        documents = [
            Document(
                page_content=chunk["original_text"],
                metadata={"summary": chunk["concise_summary"]}
            )
            for chunk in chunks
        ]

        # Create vector store
        self.vectorstore = FAISS.from_documents(documents, self.embeddings)
        return len(documents)

    def ask(self, question):
        if not self.vectorstore:
            return "No document loaded"

        # Get relevant chunks
        docs = self.vectorstore.similarity_search(question, k=3)

        return {
            "relevant_chunks": [doc.page_content for doc in docs],
            "summaries": [doc.metadata["summary"] for doc in docs]
        }

# Usage
qa = SimpleQA("your-openai-key")
qa.load_document("document.pdf")
result = qa.ask("What is the main topic?")
print(result)
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
