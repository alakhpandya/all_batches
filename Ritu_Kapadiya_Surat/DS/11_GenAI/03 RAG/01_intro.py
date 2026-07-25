# RAG: Retrieval Augmented Generation

# Why do we need RAG - Limitations of a regular LLM
"""
does NOT know your documents
does NOT know latest company data
hallucinate when the context is too big
cannot read PDFs automatically
"""

# How does RAG solve this problem?
"""
Retrieve relevant information
        ↓
Give retrieved data to LLM
        ↓
Generate accurate answer
"""

# Where is it used?
"""
ChatPDF
AI document assistants
enterprise knowledge bots / company AI assistants
"""

# Companies/Organizations using RAG heavily:
"""
OpenAI
Microsoft
Google Cloud
LangChain
LlamaIndex
"""

# Remember:
"""
RAG does not train our model/LLM
It just injects the context to the LLM in a smarter way (Smart Context Injection)
"""

# What will we build while learning RAG? AI PDF Question-Answering System.
"""
User:
    uploads PDF

AI:
    reads document
    stores chunks
    retrieves relevant information
    answers questions
"""

# The Architecture/Flow (Very Imp Diagram):
"""
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
 ↓
Similarity Search
 ↓
LLM
 ↓
Answer
"""

# Packages:
"""
pypdf -> read pdf
sentence-transformers -> create vector embedding
chromadb -> vector database
"""