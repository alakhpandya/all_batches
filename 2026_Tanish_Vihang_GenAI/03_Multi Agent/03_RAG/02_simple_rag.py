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
sentence-transformers -> create vector embedding
chromadb -> vector database
"""
from openai import OpenAI
from dotenv import load_dotenv
import os
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb
import warnings

warnings.filterwarnings("ignore")

load_dotenv()

client = OpenAI(

    base_url="https://openrouter.ai/api/v1",

    api_key=os.getenv("OPENROUTER_API_KEY")
)

print("\nClient connected to OperRouter successfully...\n")


# ----------------------- Loading pdf -----------------------

# pdf_path = "harsh.pdf"
pdf_path = "mohit.pdf"

reader = PdfReader(pdf_path)

document_text = ""

for page in reader.pages:
    document_text += page.extract_text()

print("\nPdf loaded successfully...\n")
# print("Document text:\n", document_text, "\n")


# ----------------------- Chunking -----------------------

chunk_size = 100

chunks = []

for i in range(0, len(document_text), chunk_size):      # i = 0, 500, 1000, 1500....
    chunks.append(document_text[i : i+chunk_size])

print(f"\nTotal chunks created = {len(chunks)}\n")
# print(chunks)


# ----------------------- Vector Embedding Model -----------------------
embedding_model = SentenceTransformer(
    "multi-qa-mpnet-base-cos-v1"
)
print("\nEmbedding Model Instance created\n")


# ----------------------- Vector Database - ChromaDB -----------------------
chromadb_client = chromadb.Client()

collection = chromadb_client.create_collection(
    name= "pdf_rag"
)

print("\nVector Database Created\n")

# ----------------------- Storing Vector Embeddings in the database -----------------------

for index, chunk in enumerate(chunks):
    embedding = embedding_model.encode(chunk).tolist()
    # print(f"Chunk-{index} is converted to vector")

    collection.add(
        ids= [str(index)],

        embeddings= [embedding],

        documents= [chunk]
    )
    # print(f"Embedding of Chunk-{index} is stored into vector database")

print("\nEmbeddings are stored successfully.\n")

# ----------------------- User Query -----------------------

question = input("Ask something from the document...\n[You]: ")

# Creating vector embedding of the question
question_embedding = embedding_model.encode(question).tolist()

# ----------------------- Similarity Search -----------------------

result = collection.query(
    query_embeddings= [question_embedding],

    n_results= 5
)

# print(result)
# print(result["documents"][0])
retrieved_text = "\n\n".join(result["documents"][0])
# print(retrieved_text)

# --------------------- LLM Call ---------------------
prompt = f"""
Answer the question ONLY from the the context provided.

context = {retrieved_text}

question = {question}
"""

response = client.chat.completions.create(
    
    model = "deepseek/deepseek-chat",

    messages=[{
        "role" : "user",
        "content" : prompt
    }]
    
)

print("Final answer from the AI:\n")
print(response.choices[0].message.content)