# Docker Setup

Kallia provides comprehensive Docker support for both development and production deployments. This guide covers Docker setup, configuration, and deployment strategies based on the actual Docker configurations.

## Overview

Kallia consists of two main services:

- **Core API Service**: FastAPI-based document processing service
- **Playground**: Chainlit-powered interactive chat interface

Each service can be deployed independently using Docker and Docker Compose.

## Prerequisites

- Docker 20.10 or higher
- Docker Compose 2.0 or higher
- Ollama running locally (for AI model inference)
- 4GB+ RAM recommended
- 2GB+ disk space

## Quick Start

### 1. Core API Service

Navigate to the core directory and start the service:

```bash
cd kallia/core
docker-compose up -d
```

The API will be available at `http://localhost:8000`

### 2. Playground Service

Navigate to the playground directory and start the service:

```bash
cd kallia/playground
docker-compose up -d
```

The playground will be available at `http://localhost:8000`

## Core API Service

### Docker Compose Configuration

The core service uses the following `docker-compose.yml`:

```yaml
name: kallia
services:
  core:
    image: overheatsystem/kallia:0.1.4
    container_name: core
    ports:
      - "8000:80"
    environment:
      - KALLIA_PROVIDER_API_KEY=ollama
      - KALLIA_PROVIDER_BASE_URL=http://localhost:11434/v1
      - KALLIA_PROVIDER_MODEL=qwen2.5vl:32b
```

### Dockerfile

The core service uses this Dockerfile:

```dockerfile
FROM python:3.11-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./kallia_core /code/kallia_core
CMD ["fastapi", "run", "kallia_core/main.py", "--port", "80"]
```

### Environment Configuration

Create a `.env` file in the core directory:

```bash
# Copy the example file
cp .env.example .env
```

The `.env.example` file contains:

```bash
KALLIA_PROVIDER_API_KEY=ollama
KALLIA_PROVIDER_BASE_URL=http://localhost:11434/v1
KALLIA_PROVIDER_MODEL=qwen2.5vl:32b
```

### Manual Docker Commands

Using the pre-built image from Docker Hub:

```bash
docker run -d \
  --name kallia-core \
  -p 8000:80 \
  -e KALLIA_PROVIDER_API_KEY=ollama \
  -e KALLIA_PROVIDER_BASE_URL=http://localhost:11434/v1 \
  -e KALLIA_PROVIDER_MODEL=qwen2.5vl:32b \
  overheatsystem/kallia:0.1.4
```

Building locally:

```bash
cd kallia/core
docker build -t kallia-core .
docker run -d \
  --name kallia-core \
  -p 8000:80 \
  --env-file .env \
  kallia-core
```

## Playground Service

### Docker Compose Configuration

The playground service uses the following `docker-compose.yml`:

```yaml
name: kallia
services:
  playground:
    build: .
    container_name: playground
    ports:
      - "8000:80"
    environment:
      - KALLIA_PROVIDER_API_KEY=ollama
      - KALLIA_PROVIDER_BASE_URL=http://localhost:11434/v1
      - KALLIA_PROVIDER_MODEL=qwen2.5vl:32b
```

### Dockerfile

The playground service uses this Dockerfile:

```dockerfile
FROM python:3.11-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./kallia_playground /code/kallia_playground
CMD ["chainlit", "run", "kallia_playground/main.py", "--host", "0.0.0.0", "--port", "80"]
```

### Environment Configuration

Create a `.env` file in the playground directory:

```bash
# Copy the example file
cp .env.example .env
```

The `.env.example` file contains:

```bash
KALLIA_PROVIDER_API_KEY=ollama
KALLIA_PROVIDER_BASE_URL=http://localhost:11434/v1
KALLIA_PROVIDER_MODEL=qwen2.5vl:32b
```

### Manual Docker Commands

Build and run the playground:

```bash
cd kallia/playground
docker build -t kallia-playground .
docker run -d \
  --name kallia-playground \
  -p 8000:80 \
  --env-file .env \
  kallia-playground
```

## Ollama Setup

Kallia requires Ollama to be running locally for AI model inference.

### Install Ollama

```bash
# Install Ollama (Linux/macOS)
curl -fsSL https://ollama.ai/install.sh | sh

# Or download from https://ollama.ai/download
```

### Pull Required Model

```bash
# Pull the Qwen2.5 VL 32B model
ollama pull qwen2.5vl:32b
```

### Start Ollama Service

```bash
# Start Ollama service
ollama serve
```

Ollama will be available at `http://localhost:11434`

## Environment Variables

### Core Configuration

- `KALLIA_PROVIDER_API_KEY`: API key for the provider (set to "ollama" for local Ollama)
- `KALLIA_PROVIDER_BASE_URL`: Base URL for the AI provider API
- `KALLIA_PROVIDER_MODEL`: Model name to use for processing

### Custom Configuration

You can modify the environment variables to use different AI providers:

```bash
# For OpenAI
KALLIA_PROVIDER_API_KEY=your-openai-api-key
KALLIA_PROVIDER_BASE_URL=https://api.openai.com/v1
KALLIA_PROVIDER_MODEL=gpt-4-vision-preview

# For Azure OpenAI
KALLIA_PROVIDER_API_KEY=your-azure-api-key
KALLIA_PROVIDER_BASE_URL=https://your-resource.openai.azure.com/
KALLIA_PROVIDER_MODEL=gpt-4-vision
```

## Docker Hub Images

Pre-built images are available on Docker Hub:

- **Core Service**: `overheatsystem/kallia:0.1.4`
- **Latest**: `overheatsystem/kallia:latest`

```bash
# Pull the latest image
docker pull overheatsystem/kallia:latest

# Run with Docker Hub image
docker run -d \
  --name kallia-core \
  -p 8000:80 \
  -e KALLIA_PROVIDER_API_KEY=ollama \
  -e KALLIA_PROVIDER_BASE_URL=http://localhost:11434/v1 \
  -e KALLIA_PROVIDER_MODEL=qwen2.5vl:32b \
  overheatsystem/kallia:latest
```

## Network Configuration

### Docker Network

Both services use the default Docker network. For custom networking:

```yaml
networks:
  kallia-network:
    driver: bridge

services:
  core:
    networks:
      - kallia-network
```

### Connecting Services

If running both core and playground together:

```yaml
version: "3.8"
services:
  core:
    image: overheatsystem/kallia:0.1.4
    ports:
      - "8000:80"
    networks:
      - kallia-network

  playground:
    build: ./playground
    ports:
      - "8001:80"
    networks:
      - kallia-network
    depends_on:
      - core

networks:
  kallia-network:
    driver: bridge
```

## Security Considerations

### Environment Security

- Use `.env` files for sensitive configuration
- Never commit `.env` files to version control
- Use Docker secrets for production deployments
- Regularly update base images and dependencies

### Network Security

- Use custom networks to isolate services
- Implement reverse proxy for production
- Enable HTTPS for external access
- Restrict container capabilities

## Next Steps

- Explore [configuration options](configuration.md) for advanced setup
- Learn about [REST API](rest-api.md) endpoints
- Check [use cases](../use-cases/) for practical implementations
- Review [core library](core.md) for direct integration

## Support

For Docker-related issues:

- GitHub Issues: [https://github.com/kallia-project/kallia/issues](https://github.com/kallia-project/kallia/issues)
- Docker Hub: [https://hub.docker.com/r/overheatsystem/kallia](https://hub.docker.com/r/overheatsystem/kallia)
- Email: [ck@kallia.net](mailto:ck@kallia.net)
