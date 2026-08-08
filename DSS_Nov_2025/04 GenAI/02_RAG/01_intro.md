# RAG: Retrieval Augmented Generation

## Why do we need RAG - Limitations of a regular LLM
- LLM is trained on general language and general knowledge, it does not have knowledge about your company or a specific document(s)
- LLMs cannot read pdf by default
- LLMs are not very good at extracting the information when the document is too big and hence may halucinate

## How does RAG solve these problems?
```
        Document/pdf
            ↓
Retrieve relevant information
            ↓
  Give retrieved data to LLM
            ↓
   Generate accurate answer

```

## Where is it used?
- Most AI Document Assistants
- All the knowledge bots of enterprises / a company's AI chatbot or AI assistants

## Which companies use RAG heavily?
- ChatPDF
- OpenAI
- Microsoft
- Google Cloud
- LangChain
- LlamaIndex

# What will we build?
```
System -> 
    - upload pdf

User -> 
    - ask a question from the pdf

AI Assistant ->
    - Read the entire document & the question
    - Retrieve the relevant information
    - Generate the answer
```

## The Architecture/Flow (Very Imp Diagram):
```
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
     User Query
         ↓
     Embeddings
         ↓
 Similarity Search
         ↓
        LLM
         ↓
       Answer
```

# Packages
- pypdf                 =>  extracts text from the pdf
- sentence-transformer  =>  creates vector embeddings
- chromadb              =>  vector database