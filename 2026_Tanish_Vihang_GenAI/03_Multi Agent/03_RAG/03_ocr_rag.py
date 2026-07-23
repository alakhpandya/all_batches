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

print("\nClient connected to OperRouter successfully...\n")

# ----------------------- OCR Reader -----------------------

image_path = "mohit.jpg"

reader = easyocr.Reader(lang_list=["en"])

result = reader.readtext(image=image_path)

# print("Length of result:", len(result))
# print(result)

# document_text = ""
for item in result:
    # print(item)
    # break
    # item[1]
    document_text = document_text + item[1] + " "

print("\nOCR Text:\n")
print(document_text)


# ----------------------- Chunking -----------------------

chunk_size = 300

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