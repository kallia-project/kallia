# Form Filling

Extract structured data from conversations using Kallia's memory API to automatically fill forms based on chat history.

## Overview

Form filling with Kallia involves using conversation history to extract and organize information into structured forms. The memory API analyzes chat interactions to identify key data points for form completion.

## Registration Form Example

### Conversation Flow

```python
import requests

# Simulate a registration conversation
conversation = [
    {"role": "assistant", "content": "Hi! I'd like to help you register. What's your full name?"},
    {"role": "user", "content": "My name is John Smith"},
    {"role": "assistant", "content": "Great! What's your email address?"},
    {"role": "user", "content": "It's john.smith@email.com"},
    {"role": "assistant", "content": "And your phone number?"},
    {"role": "user", "content": "My phone is 555-123-4567"},
    {"role": "assistant", "content": "What's your date of birth?"},
    {"role": "user", "content": "I was born on March 15, 1990"},
    {"role": "assistant", "content": "What's your current address?"},
    {"role": "user", "content": "I live at 123 Main Street, New York, NY 10001"}
]
```

### Extract Form Data with Memory API

```python
def extract_registration_data(conversation):
    """Extract registration form data using Kallia memory API"""

    # Create memories from conversation
    response = requests.post(
        "http://localhost:8000/memories",
        json={
            "messages": conversation,
            "temperature": 0.7,
            "max_tokens": 4000
        }
    )

    memories = response.json()["memories"]

    # Parse memories to extract form fields
    form_data = parse_memories_for_registration(memories)

    return form_data

def parse_memories_for_registration(memories):
    """Parse memories to extract registration form fields"""

    # The memory API extracts key information from conversations
    # This is a simplified example of how to process the memories

    form_fields = {
        "full_name": None,
        "email": None,
        "phone": None,
        "date_of_birth": None,
        "address": None
    }

    # Extract information from memory structure
    # (The actual memory structure depends on the AI model's output)

    if "personal_information" in memories:
        personal_info = memories["personal_information"]

        # Extract name
        if "name" in personal_info:
            form_fields["full_name"] = personal_info["name"]

        # Extract contact information
        if "contact" in personal_info:
            contact = personal_info["contact"]
            form_fields["email"] = contact.get("email")
            form_fields["phone"] = contact.get("phone")

        # Extract other details
        form_fields["date_of_birth"] = personal_info.get("birth_date")
        form_fields["address"] = personal_info.get("address")

    return form_fields

# Usage
form_data = extract_registration_data(conversation)
print("Extracted Registration Data:")
for field, value in form_data.items():
    print(f"{field}: {value}")
```

## Best Practices

### Conversation Design

- **Clear Questions**: Ask one piece of information at a time
- **Confirmation**: Confirm important details with the user
- **Natural Flow**: Make the conversation feel natural and friendly
- **Error Handling**: Handle unclear or incomplete responses gracefully

### Memory Utilization

- **Context Preservation**: Use the full conversation history for better extraction
- **Progressive Enhancement**: Build up information over multiple turns
- **Validation**: Cross-reference extracted data for consistency
- **Fallback**: Have fallback questions if extraction fails

### Data Quality

- **Validation**: Validate extracted data format (email, phone, etc.)
- **Completeness**: Check for required fields before form submission
- **Accuracy**: Allow users to review and correct extracted information
- **Privacy**: Handle sensitive information appropriately

## Common Use Cases

### Customer Registration

- Collect personal information through natural conversation
- Extract contact details and preferences
- Build customer profiles from chat interactions

### Support Ticket Creation

- Gather issue details through conversation
- Extract problem description and urgency
- Collect user environment and context information

### Survey Collection

- Conduct surveys through conversational interface
- Extract opinions and feedback naturally
- Analyze sentiment and satisfaction levels

### Lead Qualification

- Qualify sales leads through conversation
- Extract company information and requirements
- Identify decision makers and budget information

## Next Steps

- Try [Document Q&A](document-qa.md) for document-based interactions
- Learn about [REST API](../fundamentals/rest-api.md) for integration
