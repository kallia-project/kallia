# 🛠️ Getting set up

Get started with Kallia in minutes using either PyPI or Docker. Choose the installation method that best fits your development workflow.

## Prerequisites

Before installing Kallia, ensure you have:

- **Python 3.11 or higher** (for PyPI installation)
- **Docker and Docker Compose** (for Docker installation)
- **Git** (for development installation)
- **Ollama or compatible LLM provider** (for AI processing)

## Installation Options

### Option 1: PyPI Installation (Recommended)

The easiest way to get started with Kallia is through PyPI:

<details>

<summary>Step 1: Install Kallia</summary>

Install Kallia using pip:

```bash
pip install kallia
```

</details>

<details>

<summary>Step 2: Configure Environment</summary>

Create a `.env` file with your LLM provider configuration:

```bash
# LLM Provider Configuration
KALLIA_PROVIDER_API_KEY=ollama
KALLIA_PROVIDER_BASE_URL=http://localhost:11434/v1
KALLIA_PROVIDER_MODEL=qwen2.5vl:32b
```

**For Ollama (Default):**

- Install Ollama from [https://ollama.ai](https://ollama.ai)
- Pull the required model: `ollama pull qwen2.5vl:32b`
- Start Ollama service

**For OpenAI:**

```bash
KALLIA_PROVIDER_API_KEY=your_openai_api_key
KALLIA_PROVIDER_BASE_URL=https://api.openai.com/v1
KALLIA_PROVIDER_MODEL=gpt-4o-mini
```

</details>

<details>

<summary>Step 3: Verify Installation</summary>

Verify your installation by importing Kallia:

```python
from kallia_core.documents import Documents
from kallia_core.chunker import Chunker
from kallia_core.memories import Memories

print("Kallia installed successfully!")
```

</details>

### Option 2: Docker Installation

For containerized deployment and development:

<details>

<summary>Step 1: Clone the Repository</summary>

```bash
git clone https://github.com/kallia-project/kallia.git
cd kallia
```

</details>

<details>

<summary>Step 2: Configure Environment</summary>

Set up environment variables for both core and playground services:

**Core Service:**

```bash
cd kallia/core
cp .env.example .env
# Edit .env with your LLM provider configuration
```

**Playground Service:**

```bash
cd kallia/playground
cp .env.example .env
# Edit .env with your LLM provider configuration
```

Example `.env` configuration:

```bash
# For Ollama (default)
KALLIA_PROVIDER_API_KEY=ollama
KALLIA_PROVIDER_BASE_URL=http://localhost:11434/v1
KALLIA_PROVIDER_MODEL=qwen2.5vl:32b

# For OpenAI
# KALLIA_PROVIDER_API_KEY=your_openai_api_key
# KALLIA_PROVIDER_BASE_URL=https://api.openai.com/v1
# KALLIA_PROVIDER_MODEL=gpt-4o-mini
```

</details>

<details>

<summary>Step 3: Start Core API Service</summary>

Launch the core API service using Docker Compose:

```bash
cd kallia/core
docker-compose up -d
```

The core API will be available at `http://localhost:8000`

</details>

<details>

<summary>Step 4: Start Playground (Optional)</summary>

Launch the interactive playground:

```bash
cd kallia/playground
docker-compose up -d
```

The playground will be available at `http://localhost:8000`

Access the Chainlit interface for interactive document Q&A.

</details>

## Quick Start Examples

### Python API Usage

```python
from kallia_core.documents import Documents
from kallia_core.chunker import Chunker
from kallia_core.memories import Memories

# Process a document
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

### REST API Usage

```bash
# Process a document
curl -X POST "http://localhost:8000/documents" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "path/to/your/document.pdf",
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

### Getting Help

- **Documentation**: Check our comprehensive guides
- **GitHub Issues**: [Report bugs or request features](https://github.com/kallia-project/kallia/issues)
- **API Docs**: Visit `http://localhost:8000/docs` for interactive API documentation

## Next Steps

Now that you have Kallia installed, explore:

- [Document Chunking Use Case](../../use-cases/document-chunking.md)
- [Memory Generation Use Case](../../use-cases/memory-generation.md)
- [API Reference](http://localhost:8000/docs) (when server is running)

Ready to start processing documents intelligently with Kallia!
