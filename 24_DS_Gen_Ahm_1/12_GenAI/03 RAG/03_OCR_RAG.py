"""
Image PDF
    ↓
OCR Extraction
    ↓
Text Cleaning
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector DB
    ↓
Retrieval of Relavant Information (RAG)
    ↓
LLM Answering
"""

from openai import OpenAI
from dotenv import load_dotenv
import os
import chromadb
from sentence_transformers import SentenceTransformer

import easyocr

load_dotenv()

client = OpenAI(

    base_url="https://openrouter.ai/api/v1",

    api_key=os.getenv("OPENROUTER_API_KEY")
)


# --------------------- OCR Reader ---------------------
image_pdf_path = "mohit.jpg"

reader = easyocr.Reader(["en"])

result = reader.readtext(image_pdf_path)

document_text = ""

for item in result:
    # print(item)
    # break
    document_text = document_text + item[1] + " "

print("\nOCR Text\n")
print(document_text)


# --------------------- Chunking ---------------------

chunk_size = 300

chunks = [

    document_text[i : i + chunk_size]

    for i in range(0, len(document_text), chunk_size)

]

print(f"Total chunks created: {len(chunks)}\n")

# --------------------- Embedding Model ---------------------

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# --------------------- Chroma DB ---------------------
chromadb_client = chromadb.Client()

collection = chromadb_client.create_collection(
    name="ocr_rag"
)

# --------------------- Store Embeddings ---------------------

for index, chunk in enumerate(chunks):
    embedding = embedding_model.encode(chunk).tolist()
    collection.add(
        ids= [str(index)],

        embeddings= [embedding],

        documents= [chunk]
    )

print("\nEmbeddings are stored successfully.\n")

# --------------------- User Question ---------------------

question = input("Ask a question from the pdf\n")

# creating vector embedding of the question
question_embedding = embedding_model.encode(question).tolist()


# --------------------- Vector Similarity Search ---------------------

result = collection.query(
    query_embeddings= [question_embedding],

    n_results=2
)

retrieved_text = "\n".join(result["documents"][0])
print("\nContext:\n", retrieved_text, "\n\n")

# --------------------- LLM Call ---------------------

prompt = f"""
Answer the question ONLY using the provided context.

context: {retrieved_text}

question: {question}
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