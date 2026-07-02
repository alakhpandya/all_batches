from openai import OpenAI
from dotenv import load_dotenv
import os
from pypdf import PdfReader
import chromadb
from sentence_transformers import SentenceTransformer


load_dotenv()

client = OpenAI(

    base_url="https://openrouter.ai/api/v1",

    api_key=os.getenv("OPENROUTER_API_KEY")
)

# --------------------- Load pdf ---------------------

pdf_path = "harsh.pdf"

reader = PdfReader(pdf_path)

document_text = ""

for page in reader.pages:
    document_text += page.extract_text()

print("\nPDF loaded successfully!\n")
# print(document_text)

# --------------------- Chunking ---------------------

chunk_size = 500

chunks = []
for i in range(0, len(document_text), chunk_size):
    chunks.append(document_text[i : i + chunk_size])

print(f"Total chunks created: {len(chunks)}\n")
# print(chunks)

# --------------------- Embedding Model ---------------------

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# --------------------- Chroma DB ---------------------
chromadb_client = chromadb.Client()

collection = chromadb_client.create_collection(
    name="pdf_rag"
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

# print(collection.get(ids="0", include=["documents", "embeddings"]))

# --------------------- User Question ---------------------

question = input("Ask a question from the pdf\n")

# creating vector embedding of the question
question_embedding = embedding_model.encode(question).tolist()


# --------------------- Vector Similarity Search ---------------------

result = collection.query(
    query_embeddings= [question_embedding],

    n_results=2
)

# print(result["documents"])
retrieved_text = "\n".join(result["documents"][0])

# print("\nRetrieved text:\n")
# print(retrieved_text)


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