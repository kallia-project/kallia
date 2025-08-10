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

## Complete Form Filling System

```python
import requests
from typing import List, Dict, Any

class ConversationFormFiller:
    def __init__(self):
        self.conversation_history = []
        self.extracted_data = {}

    def add_message(self, role: str, content: str):
        """Add a message to the conversation"""
        self.conversation_history.append({
            "role": role,
            "content": content
        })

    def extract_form_data(self, form_type: str = "registration"):
        """Extract form data from conversation history"""

        if not self.conversation_history:
            return {"error": "No conversation history available"}

        # Use Kallia memory API
        response = requests.post(
            "http://localhost:8000/memories",
            json={
                "messages": self.conversation_history,
                "temperature": 0.7,
                "max_tokens": 4000
            }
        )

        if response.status_code != 200:
            return {"error": "Failed to process memories"}

        memories = response.json()["memories"]

        # Extract data based on form type
        if form_type == "registration":
            return self.extract_registration_form(memories)
        elif form_type == "contact":
            return self.extract_contact_form(memories)
        elif form_type == "survey":
            return self.extract_survey_form(memories)
        else:
            return {"error": f"Unknown form type: {form_type}"}

    def extract_registration_form(self, memories):
        """Extract registration form fields"""

        form_data = {
            "form_type": "registration",
            "fields": {
                "full_name": self.find_in_memories(memories, ["name", "full name"]),
                "email": self.find_in_memories(memories, ["email", "email address"]),
                "phone": self.find_in_memories(memories, ["phone", "phone number", "mobile"]),
                "date_of_birth": self.find_in_memories(memories, ["birth", "birthday", "born"]),
                "address": self.find_in_memories(memories, ["address", "location", "live"]),
                "occupation": self.find_in_memories(memories, ["job", "work", "occupation"]),
                "company": self.find_in_memories(memories, ["company", "employer"])
            },
            "confidence": self.calculate_confidence(memories),
            "source": "conversation_memory"
        }

        return form_data

    def extract_contact_form(self, memories):
        """Extract contact form fields"""

        form_data = {
            "form_type": "contact",
            "fields": {
                "name": self.find_in_memories(memories, ["name"]),
                "email": self.find_in_memories(memories, ["email"]),
                "subject": self.find_in_memories(memories, ["subject", "about", "regarding"]),
                "message": self.find_in_memories(memories, ["message", "inquiry", "question"]),
                "preferred_contact": self.find_in_memories(memories, ["contact", "reach", "prefer"])
            },
            "confidence": self.calculate_confidence(memories),
            "source": "conversation_memory"
        }

        return form_data

    def extract_survey_form(self, memories):
        """Extract survey form responses"""

        form_data = {
            "form_type": "survey",
            "fields": {
                "satisfaction": self.find_in_memories(memories, ["satisfied", "happy", "rating"]),
                "feedback": self.find_in_memories(memories, ["feedback", "opinion", "think"]),
                "recommendations": self.find_in_memories(memories, ["recommend", "suggest", "improve"]),
                "future_interest": self.find_in_memories(memories, ["future", "interested", "again"])
            },
            "confidence": self.calculate_confidence(memories),
            "source": "conversation_memory"
        }

        return form_data

    def find_in_memories(self, memories, keywords):
        """Find information in memories based on keywords"""

        # This is a simplified search function
        # In practice, the memory structure would be more sophisticated

        memory_text = str(memories).lower()

        for keyword in keywords:
            if keyword in memory_text:
                # Extract context around the keyword
                # This is a basic implementation
                return f"Found: {keyword} in memories"

        return None

    def calculate_confidence(self, memories):
        """Calculate confidence score for extracted data"""

        # Simple confidence calculation based on memory completeness
        if not memories:
            return 0.0

        # Count non-empty fields or memory sections
        confidence = min(len(str(memories)) / 1000, 1.0)
        return round(confidence, 2)

    def get_conversation_summary(self):
        """Get a summary of the conversation"""

        if not self.conversation_history:
            return "No conversation history"

        response = requests.post(
            "http://localhost:8000/memories",
            json={
                "messages": self.conversation_history,
                "temperature": 0.7,
                "max_tokens": 4000
            }
        )

        if response.status_code == 200:
            memories = response.json()["memories"]
            return memories
        else:
            return "Failed to generate summary"

# Usage Example
form_filler = ConversationFormFiller()

# Simulate a registration conversation
form_filler.add_message("assistant", "Hi! Let's get you registered. What's your name?")
form_filler.add_message("user", "Hi, I'm Sarah Johnson")
form_filler.add_message("assistant", "Nice to meet you Sarah! What's your email?")
form_filler.add_message("user", "My email is sarah.johnson@gmail.com")
form_filler.add_message("assistant", "Great! And your phone number?")
form_filler.add_message("user", "It's 555-987-6543")
form_filler.add_message("assistant", "When were you born?")
form_filler.add_message("user", "I was born on July 22, 1985")
form_filler.add_message("assistant", "What's your current address?")
form_filler.add_message("user", "I live at 456 Oak Avenue, Los Angeles, CA 90210")

# Extract registration form data
registration_data = form_filler.extract_form_data("registration")
print("Registration Form Data:")
print(registration_data)

# Get conversation summary
summary = form_filler.get_conversation_summary()
print("\nConversation Summary:")
print(summary)
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
