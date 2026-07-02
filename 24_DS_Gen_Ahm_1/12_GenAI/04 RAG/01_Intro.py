# RAG: Retrieval Augmented Generation

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

# Why do we use RAG - Limitations of a regular LLM
"""
do NOT know your documents
do NOT know latest company data
hallucinate
cannot read PDFs automatically
"""

# How RAG solves this problem?
"""
Retrieve relevant information
        ↓
Give retrieved data to LLM
        ↓
Generate accurate answer
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
chromadb -> vector database
sentence-transformers -> create vector embedding
"""