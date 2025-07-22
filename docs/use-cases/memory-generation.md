# 🧠 Memory Generation

Learn how to create memories from conversations using Kallia.

## What is Memory Generation?

Memory generation turns conversation histories into structured memories. This helps AI systems remember important information from past conversations.

## Basic Example

### Step 1: Prepare Messages

```python
from kallia_core.memories import Memories

# Example conversation
messages = [
    {"role": "user", "content": "I'm working on a Python project"},
    {"role": "assistant", "content": "What kind of Python project?"},
    {"role": "user", "content": "A web scraper using BeautifulSoup"},
    {"role": "assistant", "content": "That's great! Need help with any specific part?"}
]
```

### Step 2: Create Memories

```python
# Generate memories
memories = Memories.create(
    messages=messages,
    temperature=0.7,
    max_tokens=4000
)

print(f"Created {len(memories)} memories:")
for i, memory in enumerate(memories, 1):
    print(f"{i}. {memory}")
```

## REST API Example

```bash
curl -X POST "http://localhost:8000/memories" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "I need help with Python"},
      {"role": "assistant", "content": "What do you need help with?"},
      {"role": "user", "content": "Learning pandas for data analysis"}
    ],
    "temperature": 0.7,
    "max_tokens": 4000
  }'
```

## Common Use Cases

### 1. Customer Support

```python
# Remember customer issues
messages = [
    {"role": "user", "content": "My order #12345 is late"},
    {"role": "assistant", "content": "Let me check that for you"},
    {"role": "user", "content": "I need it by Friday"}
]

memories = Memories.create(messages=messages)
```

### 2. Learning Sessions

```python
# Remember what user is learning
messages = [
    {"role": "user", "content": "I'm learning calculus"},
    {"role": "assistant", "content": "Which topic in calculus?"},
    {"role": "user", "content": "Derivatives are confusing me"}
]

memories = Memories.create(messages=messages)
```

## Parameter Tips

### Temperature

- **0.3-0.5**: For factual conversations
- **0.5-0.7**: For general conversations
- **0.7-0.9**: For creative conversations

### Max Tokens

- **2000-3000**: Short conversations
- **3000-4000**: Medium conversations
- **4000+**: Long conversations

## Simple Tips

1. **Include full conversations**: More context = better memories
2. **Use lower temperature for facts**: More accurate memories
3. **Generate memories regularly**: After important conversations
4. **Check memory quality**: Make sure they capture key information

## Troubleshooting

**Memories not specific enough?**

- Lower the temperature
- Include more conversation context

**Missing important details?**

- Increase max_tokens
- Include more messages

## Next Steps

- Try [Document Chunking](document-chunking.md) for processing documents
- Check the [API docs](http://localhost:8000/docs) for more features
- See the [setup guide](../fundamentals/getting-set-up/) for installation help
