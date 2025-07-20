# Kallia

[![Version](https://img.shields.io/badge/version-0.1.3-blue.svg)](https://github.com/kallia-project/kallia)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://python.org)
[![Docker](https://img.shields.io/badge/docker-overheatsystem%2Fkallia-blue.svg)](https://hub.docker.com/r/overheatsystem/kallia)

**Kallia** is a semantic document processing library that converts documents into intelligent semantic chunks. The library specializes in extracting meaningful content segments from documents while preserving context and semantic relationships.

## 🚀 Features

- **Document-to-Markdown Conversion**: Standardized processing pipeline for various document formats
- **Semantic Chunking**: Intelligent content segmentation that respects document structure and meaning
- **PDF Support**: Robust PDF processing with extensible architecture for additional formats
- **RESTful API**: FastAPI-based service with comprehensive error handling
- **Interactive Playground**: Chainlit-powered chat interface for document Q&A
- **Memory Management**: Long-term and short-term memory systems for conversational context
- **Configurable Processing**: Adjustable parameters (temperature, token limits, page selection)
- **Docker Support**: Containerized deployment for both core API and playground

## 📋 Requirements

- Python 3.11 or higher
- FastAPI 0.115.14
- Docling 2.41.0

## 🛠️ Installation

### Using pip

```bash
pip install kallia
```

### From Source

```bash
git clone https://github.com/kallia-project/kallia.git
cd kallia
pip install -e .
```

## 🏗️ Project Structure

```
kallia/
├── kallia/
│   ├── core/                    # Core API service
│   │   ├── kallia_core/         # Main library modules
│   │   │   ├── main.py          # FastAPI application
│   │   │   ├── documents.py     # Document processing
│   │   │   ├── chunker.py       # Semantic chunking
│   │   │   ├── memories.py      # Memory management
│   │   │   ├── models.py        # Data models
│   │   │   └── ...
│   │   ├── requirements.txt     # Core dependencies
│   │   ├── Dockerfile          # Core service container
│   │   └── docker-compose.yml  # Core service orchestration
│   └── playground/             # Interactive chat interface
│       ├── kallia_playground/  # Playground modules
│       │   ├── main.py         # Chainlit application
│       │   ├── qa.py           # Q&A functionality
│       │   └── ...
│       ├── requirements.txt    # Playground dependencies
│       ├── Dockerfile         # Playground container
│       └── docker-compose.yml # Playground orchestration
├── tests/                     # Test suite
├── assets/                    # Sample documents
└── pyproject.toml            # Project configuration
```

## 🚀 Quick Start

### 1. Core API Service

Start the FastAPI service:

```bash
cd kallia/core
pip install -r requirements.txt
uvicorn kallia_core.main:app --reload
```

The API will be available at `http://localhost:8000`

#### API Endpoints

**Process Documents**

```bash
POST /documents
```

Request body:

```json
{
  "url": "path/to/document.pdf",
  "page_number": 1,
  "temperature": 0.7,
  "max_tokens": 4000
}
```

**Create Memories**

```bash
POST /memories
```

Request body:

```json
{
  "messages": [
    { "role": "user", "content": "Hello" },
    { "role": "assistant", "content": "Hi there!" }
  ],
  "temperature": 0.7,
  "max_tokens": 4000
}
```

### 2. Interactive Playground

Start the Chainlit chat interface:

```bash
cd kallia/playground
pip install -r requirements.txt
chainlit run kallia_playground/main.py
```

The playground will be available at `http://localhost:8000`

### 3. Docker Deployment

**Core Service**

```bash
cd kallia/core
docker-compose up -d
```

**Playground**

```bash
cd kallia/playground
docker-compose up -d
```

## 💡 Usage Examples

### Python API

```python
from kallia_core.documents import Documents
from kallia_core.chunker import Chunker
from kallia_core.memories import Memories

# Convert document to markdown
markdown_content = Documents.to_markdown(
    source="document.pdf",
    page_number=1,
    temperature=0.7,
    max_tokens=4000
)

# Create semantic chunks
chunks = Chunker.create(
    text=markdown_content,
    temperature=0.7,
    max_tokens=4000
)

# Generate memories from conversation
messages = [
    {"role": "user", "content": "What is this document about?"},
    {"role": "assistant", "content": "This document discusses..."}
]
memories = Memories.create(messages)
```

### REST API

```bash
# Process a document
curl -X POST "http://localhost:8000/documents" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://raw.githubusercontent.com/kallia-project/kallia/refs/tags/v0.1.3/assets/pdf/01.pdf",
    "page_number": 1,
    "temperature": 0.7,
    "max_tokens": 4000
  }'

# Create memories
curl -X POST "http://localhost:8000/memories" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello"},
      {"role": "assistant", "content": "Hi there!"}
    ],
    "temperature": 0.7,
    "max_tokens": 4000
  }'
```

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/
```

Available tests:

- `test_pdf_to_markdown.py` - Document conversion tests
- `test_markdown_to_chunks.py` - Chunking functionality tests
- `test_histories_to_memories.py` - Memory creation tests

## 🔧 Configuration

### Environment Variables

Create a `.env` file based on the provided `.env.example` template in each directory:

**Core Service**:

```bash
cd kallia/core
cp .env.example .env
# Edit .env with your configuration
```

**Playground**:

```bash
cd kallia/playground
cp .env.example .env
# Edit .env with your configuration
```

### Supported File Formats

Currently supported:

- PDF documents

The architecture is designed to be extensible for additional formats.

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Homepage**: [https://github.com/kallia-project/kallia](https://github.com/kallia-project/kallia)
- **Docker Hub**: [https://hub.docker.com/r/overheatsystem/kallia](https://hub.docker.com/r/overheatsystem/kallia)
- **Issues**: [https://github.com/kallia-project/kallia/issues](https://github.com/kallia-project/kallia/issues)
- **Documentation**: Coming soon

## 👨‍💻 Author

**CK** - [ck@kallia.net](mailto:ck@kallia.net)

## 🏷️ Keywords

- document-processing
- semantic-chunking
- document-analysis
- text-processing
- machine-learning
- fastapi
- chainlit
- pdf-processing
- nlp
- ai

---

Built with ❤️ for intelligent document processing
