# REST API Reference

Kallia provides a comprehensive RESTful API built with FastAPI for document processing, semantic chunking, and memory management. This guide covers all available endpoints, request/response formats, and usage examples.

## Base URL

When running locally:

```
http://localhost:8000
```

## API Overview

The Kallia API provides four main endpoints:

- `POST /documents` - Complete document processing pipeline
- `POST /markdownify` - Document to markdown conversion
- `POST /chunks` - Text to semantic chunks conversion
- `POST /memories` - Conversation memory generation

## Authentication

Currently, the API does not require authentication. For production deployments, consider implementing authentication middleware.

## Content Type

All requests should use `Content-Type: application/json`.

## Endpoints

### 1. Process Documents

**Endpoint:** `POST /documents`

Complete document processing pipeline that converts a document to markdown and creates semantic chunks.

#### Request

```json
{
  "url": "string",
  "page_number": 1,
  "temperature": 0.7,
  "max_tokens": 4000,
  "include_image_captioning": false
}
```

#### Parameters

- `url` (string, required): Path or URL to the document
- `page_number` (integer, optional): Page number to process (default: 1)
- `temperature` (float, optional): AI model temperature 0.0-1.0 (default: 0.0)
- `max_tokens` (integer, optional): Maximum tokens for processing (default: 8192)
- `include_image_captioning` (boolean, optional): Enable image descriptions (default: false)

#### Response

```json
{
  "documents": [
    {
      "page_number": 1,
      "chunks": [
        {
          "original_text": "Original text content...",
          "concise_summary": "Brief summary of the content",
          "question": "What does this section discuss?",
          "answer": "This section discusses..."
        }
      ]
    }
  ]
}
```

#### Example

```bash
curl -X POST "http://localhost:8000/documents" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/document.pdf",
    "page_number": 1,
    "temperature": 0.7,
    "max_tokens": 4000,
    "include_image_captioning": true
  }'
```

### 2. Convert to Markdown

**Endpoint:** `POST /markdownify`

Converts a document to structured markdown format.

#### Request

```json
{
  "url": "string",
  "page_number": 1,
  "temperature": 0.7,
  "max_tokens": 4000,
  "include_image_captioning": false
}
```

#### Response

```json
{
  "markdown": "# Document Title\n\nDocument content in markdown format..."
}
```

#### Example

```bash
curl -X POST "http://localhost:8000/markdownify" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "document.pdf",
    "page_number": 1,
    "temperature": 0.5,
    "max_tokens": 6000
  }'
```

### 3. Create Semantic Chunks

**Endpoint:** `POST /chunks`

Converts text content into semantic chunks with summaries and Q&A pairs.

#### Request

```json
{
  "text": "string",
  "temperature": 0.7,
  "max_tokens": 4000
}
```

#### Parameters

- `text` (string, required): Text content to chunk
- `temperature` (float, optional): AI model temperature (default: 0.0)
- `max_tokens` (integer, optional): Maximum tokens for processing (default: 8192)

#### Response

```json
{
  "chunks": [
    {
      "original_text": "Original text segment...",
      "concise_summary": "Summary of this segment",
      "question": "Generated question about content",
      "answer": "Answer to the generated question"
    }
  ]
}
```

#### Example

```bash
curl -X POST "http://localhost:8000/chunks" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "This is a long document that needs to be chunked into semantic segments...",
    "temperature": 0.8,
    "max_tokens": 5000
  }'
```

### 4. Generate Memories

**Endpoint:** `POST /memories`

Creates contextual memories from conversation history.

#### Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hello, how are you?"
    },
    {
      "role": "assistant",
      "content": "I'm doing well, thank you!"
    }
  ],
  "temperature": 0.7,
  "max_tokens": 4000
}
```

#### Parameters

- `messages` (array, required): Array of conversation messages
  - `role` (string): Either "user" or "assistant"
  - `content` (string): Message content
- `temperature` (float, optional): AI model temperature (default: 0.0)
- `max_tokens` (integer, optional): Maximum tokens for processing (default: 8192)

#### Response

```json
{
  "memories": {
    "short_term": {
      "recent_context": "Summary of recent conversation",
      "topics": ["topic1", "topic2"]
    },
    "long_term": {
      "insights": "Key insights extracted",
      "patterns": ["pattern1", "pattern2"]
    },
    "relationships": {
      "connections": "Relationship mappings"
    }
  }
}
```

#### Example

```bash
curl -X POST "http://localhost:8000/memories" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "What is semantic chunking?"},
      {"role": "assistant", "content": "Semantic chunking is a process..."},
      {"role": "user", "content": "How does it work?"},
      {"role": "assistant", "content": "It works by analyzing..."}
    ],
    "temperature": 0.6,
    "max_tokens": 3000
  }'
```

## Error Handling

The API uses standard HTTP status codes and returns detailed error messages.

### Status Codes

- `200` - Success
- `400` - Bad Request (invalid parameters)
- `500` - Internal Server Error
- `503` - Service Unavailable

### Error Response Format

```json
{
  "detail": "Error description"
}
```

### Common Errors

#### 400 Bad Request

```json
{
  "detail": "Invalid File Format"
}
```

Occurs when:

- Unsupported file format is provided
- Required parameters are missing
- Invalid parameter values

#### 500 Internal Server Error

```json
{
  "detail": "Internal Server Error"
}
```

Occurs when:

- Document processing fails
- AI model errors
- Unexpected system errors

#### 503 Service Unavailable

```json
{
  "detail": "Service Unavailable"
}
```

Occurs when:

- External services are unreachable
- Network connectivity issues
- Resource limitations

## Supported File Formats

Currently supported formats:

- PDF documents

The architecture is designed to be extensible for additional formats.

## Rate Limiting

No rate limiting is currently implemented. For production use, consider implementing rate limiting middleware.

## Request Size Limits

- Maximum file size: Depends on server configuration
- Maximum request body: 100MB (configurable)
- Maximum text length: No explicit limit (limited by max_tokens)

## Python Client Examples

### Using requests library

```python
import requests
import json

# Document processing
def process_document(url, page_number=1):
    response = requests.post(
        "http://localhost:8000/documents",
        json={
            "url": url,
            "page_number": page_number,
            "temperature": 0.7,
            "max_tokens": 4000
        }
    )
    return response.json()

# Memory creation
def create_memories(messages):
    response = requests.post(
        "http://localhost:8000/memories",
        json={
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 4000
        }
    )
    return response.json()

# Usage
result = process_document("document.pdf", 1)
memories = create_memories([
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there!"}
])
```

### Using httpx (async)

```python
import httpx
import asyncio

async def async_process_document(url, page_number=1):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/documents",
            json={
                "url": url,
                "page_number": page_number,
                "temperature": 0.7,
                "max_tokens": 4000
            }
        )
        return response.json()

# Usage
result = asyncio.run(async_process_document("document.pdf"))
```

## JavaScript Client Examples

### Using fetch

```javascript
// Document processing
async function processDocument(url, pageNumber = 1) {
  const response = await fetch("http://localhost:8000/documents", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      url: url,
      page_number: pageNumber,
      temperature: 0.7,
      max_tokens: 4000,
    }),
  });

  return await response.json();
}

// Memory creation
async function createMemories(messages) {
  const response = await fetch("http://localhost:8000/memories", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      messages: messages,
      temperature: 0.7,
      max_tokens: 4000,
    }),
  });

  return await response.json();
}

// Usage
const result = await processDocument("document.pdf", 1);
const memories = await createMemories([
  { role: "user", content: "Hello" },
  { role: "assistant", content: "Hi there!" },
]);
```

## API Documentation

When the server is running, interactive API documentation is available at:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

These interfaces provide:

- Interactive endpoint testing
- Request/response schema validation
- Example requests and responses
- Parameter documentation

## Performance Considerations

### Optimization Tips

1. **Batch Processing**: Process multiple pages separately for large documents
2. **Caching**: Implement client-side caching for repeated requests
3. **Async Requests**: Use async clients for concurrent processing
4. **Parameter Tuning**: Adjust temperature and max_tokens based on use case

### Response Times

Typical response times (varies by document size and complexity):

- `/markdownify`: 2-10 seconds
- `/chunks`: 5-15 seconds
- `/documents`: 7-25 seconds
- `/memories`: 1-5 seconds

## Next Steps

- Learn about [Docker deployment](docker.md) for production setup
- Explore [use cases](../use-cases/) for practical implementations
- Check the [core library](core.md) for direct Python integration
- Review [configuration options](configuration.md) for customization

## Support

For API-related questions or issues:

- GitHub Issues: [https://github.com/kallia-project/kallia/issues](https://github.com/kallia-project/kallia/issues)
- Email: [ck@kallia.net](mailto:ck@kallia.net)
- API Documentation: `http://localhost:8000/docs`
