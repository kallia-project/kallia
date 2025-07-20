# Welcome to Kallia Playground! 🚀

**Kallia** is an intelligent document processing platform that transforms your documents into semantic chunks and enables natural language conversations about their content.

## 🎯 What You Can Do

### 📄 Document Processing

- **Upload PDF documents** up to 20MB in size
- **Automatic processing** of all pages with semantic chunking
- **Intelligent content extraction** that preserves context and meaning
- **Real-time progress tracking** during document processing

### 💬 Interactive Q&A

- **Ask questions** about your uploaded documents in natural language
- **Get contextual answers** based exclusively on document content
- **View source references** for transparency and verification
- **Maintain conversation history** with memory management

### 🧠 Smart Memory System

- **Long-term memory** for extended conversations (up to recent interactions)
- **Short-term memory** for immediate context awareness
- **Conversation categorization** for better understanding
- **Memory persistence** throughout your session

## 🔧 How It Works

1. **Upload**: Start by uploading a PDF document using the file upload interface
2. **Processing**: Kallia converts your document to markdown and creates semantic chunks
3. **Indexing**: Content is embedded and stored in a vector database for similarity search
4. **Query**: Ask questions about your document in natural language
5. **Retrieve**: The system finds relevant content chunks using semantic similarity
6. **Answer**: An AI assistant provides answers based exclusively on your document content

## 🎨 Features

### 📊 **Semantic Chunking**

Advanced text segmentation that respects document structure and maintains semantic relationships between content sections.

### 🔍 **Similarity Search**

Powered by HuggingFace embeddings to find the most relevant content for your questions.

### 📚 **Source Attribution**

Every answer includes references to the specific document sections used, ensuring transparency and enabling verification.

### 🧩 **Memory Integration**

Sophisticated memory management that helps maintain context across conversations while categorizing discussion types.

### ⚡ **Real-time Processing**

Live updates during document processing so you know exactly what's happening.

## 🚀 Getting Started

1. **Click the upload button** that appears when you start a new chat
2. **Select a PDF file** from your computer (max 20MB)
3. **Wait for processing** - you'll see progress updates for each page
4. **Start asking questions** once processing is complete!

## 💡 Tips for Best Results

### 📝 **Question Formulation**

- Be specific about what you're looking for
- Reference particular sections or topics when possible
- Ask follow-up questions to dive deeper into topics

### 🎯 **Content Scope**

- Questions are answered based **only** on uploaded document content
- The assistant cannot access external information or general knowledge
- If information isn't in your document, you'll get a clear "I don't know" response

### 🔄 **Conversation Flow**

- Build on previous questions for deeper understanding
- Use the conversation history to maintain context
- Review source references to understand answer origins

## 🛠️ Technical Details

### **Processing Pipeline**

```
PDF → Markdown → Semantic Chunks → Vector Embeddings → Searchable Index
```

### **Memory Management**

- **Long-term**: Maintains context from recent conversation history
- **Short-term**: Focuses on immediate conversation context
- **Categorization**: Automatically identifies conversation types and themes

### **AI Components**

- **Document Processing**: Docling-powered PDF to markdown conversion
- **Embeddings**: HuggingFace models for semantic understanding
- **Language Model**: OpenAI-compatible models for natural language responses
- **Vector Store**: In-memory storage for fast similarity search

## 🔒 Privacy & Security

- **Local Processing**: Documents are processed in your session only
- **No Persistence**: Files and conversations are not stored permanently
- **Session Isolation**: Each user session is completely independent
- **Memory Cleanup**: All data is cleared when you close the application

## 🆘 Troubleshooting

### **Upload Issues**

- Ensure your PDF is under 20MB
- Check that the file is a valid PDF format
- Try refreshing the page if upload fails

### **Processing Problems**

- Large documents may take longer to process
- Complex layouts might affect chunking quality
- Scanned PDFs may have reduced text extraction quality

### **Answer Quality**

- If answers seem incomplete, try rephrasing your question
- Check source references to understand what content was used
- Remember that answers are limited to document content only

---

## 🎉 Ready to Start?

Upload your first PDF document and begin exploring your content with intelligent Q&A! The system will guide you through each step of the process.

**Happy exploring!** 📖✨
