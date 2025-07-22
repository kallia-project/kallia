# 📄 Document Chunking

Learn how to break down documents into intelligent, meaningful chunks using Kallia's semantic chunking capabilities.

## What is Document Chunking?

Document chunking splits large documents into smaller pieces while preserving meaning and context. Unlike simple text splitting, Kallia's semantic chunking respects document structure and natural boundaries.

## Basic Example

### Step 1: Convert Document to Markdown

```python
from kallia_core.documents import Documents

# Process a PDF document
markdown_content = Documents.to_markdown(
    source="document.pdf",
    page_number=1,
    temperature=0.7,
    max_tokens=4000
)
```

### Step 2: Create Semantic Chunks

```python
from kallia_core.chunker import Chunker

# Create intelligent chunks
chunks = Chunker.create(
    text=markdown_content,
    temperature=0.7,
    max_tokens=4000
)

print(f"Created {len(chunks)} chunks")
```

## REST API Example

```bash
# Step 1: Process document
curl -X POST "http://localhost:8000/documents" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "document.pdf",
    "page_number": 1,
    "temperature": 0.7,
    "max_tokens": 4000
  }'
```

The response will include both the markdown content and the semantic chunks.

## Common Use Cases

### 1. Research Paper Analysis

```python
# Process academic paper
content = Documents.to_markdown(
    source="research_paper.pdf",
    temperature=0.5,  # Lower temperature for accuracy
    max_tokens=4000
)

chunks = Chunker.create(
    text=content,
    temperature=0.5,
    max_tokens=2000  # Smaller chunks for detailed analysis
)
```

### 2. Legal Document Processing

```python
# Process legal documents with high precision
content = Documents.to_markdown(
    source="contract.pdf",
    temperature=0.2,  # Very low for legal precision
    max_tokens=3000
)

chunks = Chunker.create(
    text=content,
    temperature=0.2,
    max_tokens=1500
)
```

## Parameter Guidelines

### Temperature Settings

- **0.1-0.3**: Technical/legal documents (high precision)
- **0.4-0.7**: General content (balanced)
- **0.7-0.9**: Creative content (more flexible)

### Token Limits

- **1000-2000**: Detailed analysis, small chunks
- **2000-4000**: General use, medium chunks
- **4000+**: Large context, bigger chunks

## Tips for Better Results

1. **Start with defaults**: Use `temperature=0.7` and `max_tokens=4000`
2. **Adjust for content type**: Lower temperature for technical docs
3. **Check chunk quality**: Ensure chunks make sense individually
4. **Test with your documents**: Different documents may need different settings

## Troubleshooting

**Chunks too small?**

- Increase `max_tokens`
- Lower `temperature`

**Chunks lose meaning?**

- Increase chunk size
- Check document quality

**Inconsistent results?**

- Use lower temperature
- Ensure good PDF quality

## Next Steps

- Try the [Memory Generation](memory-generation.md) use case
- Explore the [API documentation](http://localhost:8000/docs)
- Check the [installation guide](../fundamentals/getting-set-up/) for setup help
