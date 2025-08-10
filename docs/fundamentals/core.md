# Core Library

The Kallia core library provides the fundamental building blocks for semantic document processing. This section covers the main components, their functionality, and how to use them programmatically.

## Overview

The core library consists of several key modules:

- **Documents**: Document conversion and processing
- **Chunker**: Semantic chunking and content segmentation
- **Memories**: Conversation memory management
- **Models**: Data structures and validation
- **Utils**: Utility functions and helpers

## Installation

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

### Requirements

- Python 3.11 or higher
- FastAPI 0.115.14
- Docling 2.41.0
- Pydantic for data validation

## Core Components

### Documents Module

The `Documents` class handles document conversion from various formats to structured markdown.

#### Key Features

- PDF to markdown conversion using Docling
- Configurable page selection
- Image captioning support
- OCR capabilities
- Scalable image processing

#### Usage

```python
from kallia_core.documents import Documents

# Convert a PDF page to markdown
markdown_content = Documents.to_markdown(
    source="document.pdf",
    page_number=1,
    temperature=0.7,
    max_tokens=4000,
    include_image_captioning=True
)
```

#### Parameters

- `source` (str): Path or URL to the document
- `page_number` (int): Specific page to process (default: 1)
- `temperature` (float): AI model temperature for processing (default: 0.0)
- `max_tokens` (int): Maximum tokens for AI processing (default: 8192)
- `include_image_captioning` (bool): Enable image description generation (default: False)

### Chunker Module

The `Chunker` class performs semantic segmentation of text content into meaningful chunks.

#### Key Features

- Semantic understanding of content structure
- Automatic summary generation
- Question-answer pair creation
- Context-aware segmentation
- Optimized for retrieval tasks

#### Usage

```python
from kallia_core.chunker import Chunker

# Create semantic chunks from text
chunks = Chunker.create(
    text=markdown_content,
    temperature=0.7,
    max_tokens=4000
)

# Each chunk contains:
for chunk in chunks:
    print(f"Original: {chunk.original_text}")
    print(f"Summary: {chunk.concise_summary}")
    print(f"Question: {chunk.question}")
    print(f"Answer: {chunk.answer}")
```

#### Chunk Structure

Each chunk is a `Chunk` object with the following properties:

- `original_text`: The original text segment
- `concise_summary`: AI-generated summary
- `question`: Generated question about the content
- `answer`: Answer to the generated question

### Memories Module

The `Memories` class extracts and manages conversational context and insights.

#### Key Features

- Short-term conversation context
- Long-term insight extraction
- Pattern recognition
- Contextual relationship mapping
- Memory persistence

#### Usage

```python
from kallia_core.memories import Memories
from kallia_core.models import Message

# Create conversation messages
messages = [
    Message(role="user", content="What is this document about?"),
    Message(role="assistant", content="This document discusses semantic processing..."),
    Message(role="user", content="How does the chunking work?"),
    Message(role="assistant", content="The chunking algorithm analyzes...")
]

# Generate memories
memories = Memories.create(
    messages=messages,
    temperature=0.7,
    max_tokens=4000
)
```

## Advanced Usage

### Custom Processing Pipeline

```python
from kallia_core.documents import Documents
from kallia_core.chunker import Chunker
from kallia_core.memories import Memories

class DocumentProcessor:
    def __init__(self, temperature=0.7, max_tokens=4000):
        self.temperature = temperature
        self.max_tokens = max_tokens

    def process_document(self, source, page_number=1):
        # Step 1: Convert to markdown
        markdown = Documents.to_markdown(
            source=source,
            page_number=page_number,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

        # Step 2: Create semantic chunks
        chunks = Chunker.create(
            text=markdown,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

        return {
            'markdown': markdown,
            'chunks': chunks,
            'page_number': page_number
        }

# Usage
processor = DocumentProcessor(temperature=0.8, max_tokens=6000)
result = processor.process_document("research_paper.pdf", page_number=1)
```

## Next Steps

- Explore the [REST API](rest-api.md) for web service integration
- Learn about [Docker deployment](docker.md) for production use
- Check out [use cases](../use-cases/) for practical examples

## Support

For technical issues or questions about the core library:

- GitHub Issues: [https://github.com/kallia-project/kallia/issues](https://github.com/kallia-project/kallia/issues)
- Email: [ck@kallia.net](mailto:ck@kallia.net)
