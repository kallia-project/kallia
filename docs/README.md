# Kallia Documentation

Welcome to the Kallia documentation! Kallia is an advanced semantic document processing library that transforms documents into intelligent, queryable knowledge bases.

## What is Kallia?

Kallia is a powerful document processing framework that:

- **Converts documents to structured markdown** with intelligent parsing using Docling
- **Generates semantic chunks** optimized for retrieval and understanding
- **Creates contextual memories** that capture conversation history and insights
- **Provides RESTful APIs** for easy integration with FastAPI
- **Supports interactive playground** with Chainlit for document Q&A
- **Handles multiple document formats** with extensible architecture

## Quick Start

1. **Installation**: Set up Kallia using Docker or pip
2. **Configuration**: Configure your environment variables
3. **API Usage**: Start processing documents via REST API
4. **Integration**: Integrate with your applications

## Documentation Structure

- **[Overview](overview/)** - Introduction and core concepts
- **[Fundamentals](fundamentals/)** - Setup, API reference, and Docker deployment
- **[Use Cases](use-cases/)** - Practical examples and implementations

## Key Features

### 🔄 Document Processing

Transform any document into structured, searchable content with intelligent parsing and formatting using Docling library.

### 🧠 Memory Generation

Create contextual memories from conversation histories that understand relationships and provide intelligent insights.

### 🔍 Semantic Chunking

Break documents into meaningful chunks with summaries, questions, and answers optimized for retrieval and comprehension.

### 🚀 RESTful API

FastAPI-based service with comprehensive endpoints for document processing, chunking, and memory creation.

### 🎮 Interactive Playground

Chainlit-powered chat interface for real-time document Q&A with memory management and source citations.

### 📊 Benchmark Performance

![Benchmark Results](https://raw.githubusercontent.com/kallia-project/kallia/refs/tags/v0.1.4/benchmark/results.png)

Proven superior performance with 4.6/5.0 mean score and 81% perfect score rate in comprehensive RAG evaluations.

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Docker (optional, for containerized deployment)

### Quick Installation

```bash
pip install kallia
```

### Docker Deployment

```bash
# Core API Service
cd kallia/core
docker-compose up -d

# Interactive Playground
cd kallia/playground
docker-compose up -d
```

## Core Concepts

### Document Processing Pipeline

1. **Input**: PDF documents (extensible to other formats)
2. **Conversion**: Document to structured markdown using Docling
3. **Chunking**: Semantic segmentation with AI-powered analysis
4. **Output**: Structured chunks with summaries, Q&A pairs

### Memory System

- **Short-term Memory**: Recent conversation context
- **Long-term Memory**: Extracted insights and patterns
- **Contextual Understanding**: Relationship mapping between conversations

### API Architecture

- **RESTful Design**: Standard HTTP methods and status codes
- **Pydantic Models**: Type-safe request/response validation
- **Error Handling**: Comprehensive exception management
- **Scalable**: Designed for production deployment

## Next Steps

- Read the [Introduction](overview/introduction.md) for detailed concepts
- Check the [API Reference](fundamentals/rest-api.md) for endpoint documentation
- Explore [Use Cases](use-cases/) for practical implementations
- Try the [Docker Setup](fundamentals/docker.md) for quick deployment

## Support

For issues, questions, or contributions:

- GitHub: [https://github.com/kallia-project/kallia](https://github.com/kallia-project/kallia)
- Email: [ck@kallia.net](mailto:ck@kallia.net)

---

Built with ❤️ for intelligent document processing
