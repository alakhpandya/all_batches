# ------------- Loading the pdf -------------

from pypdf import PdfReader

pdf_path = "harsh.pdf"
# pdf_path = "D:\new folder\temp\harsh.pdf"   # Error
# pdf_path = "D:\\new folder\\temp\\harsh.pdf"

reader = PdfReader(stream=pdf_path)

# print("Reader object:\n", reader)

# print("Pages:\n", reader.pages)

# pdf_path = "gk-book.pdf"
# reader = PdfReader(stream=pdf_path)
# print("Pages:\n", reader.pages)

# first_page = reader.pages[0]
# print("First Page:\n", first_page)
# print("First page text:\n", first_page.extract_text())

document_text = ""

for page in reader.pages:
    # document_text = document_text + page.extract_text()
    document_text += page.extract_text()

# print("Entire text of the document:\n", document_text)

# --------------------- Intuition of RAG ---------------------
"""
Steps:
- We will break down the document in small parts ("chunks")
- We can choose any size of each of these chunks depending on our document length. Typically for bigger documents we keep it either 500 characters or 1000 characters
- We create vector embedding for each of these chunks and will store them in the vector database
- Then we will ask user for any question from the document
- We will also create vector embedding for that question
- And finally we will retrieve 3 or 5 or 10 chunks which are nearest to the vector embedding of the question (using similarity search)
- This group of chunks (converted into a single string) will act as context for our LLM
"""

# ------------- Chunking -------------
chunk_size = 500

chunks = []

for i in range(0, len(document_text), chunk_size):
    # print(i)
    chunk = document_text[i : i+chunk_size]
    chunks.append(chunk)

# print("Number of chunks created:", len(chunks))
# print("Chunks:\n", chunks)
# import numpy as np
# print("Chunks:\n", np.array(chunks))

# ------------- Creating Embedding Model -------------
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer(
    model_name_or_path= "all-MiniLM-L6-v2"
)
# print("chunk:\n", chunks[0])
# print("Vector Embedding:\n", embedding_model.encode(chunks[0]))

# ------------- Creating Vector Database -------------
import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(
    name= "simple_rag_database"
)

# ------------- Vector Embeddings Of Chunks -------------

for index, chunk in enumerate(chunks):
    embedding = embedding_model.encode(chunk)
    collection.add(
        ids= [str(index)],

        embeddings= [embedding],

        documents= [chunk]
    )

print("\nEmbeddings are stored in the vector database successfully...")
# print("The first embedding:\n", )
# print(collection.get(ids= "0"))
# print(collection.get(ids= "0", include=["documents", "embeddings"]))

# ------------- User's Question -------------
question = input("Ask anything from the document!\n[You] : ")


# ------------- Vector Embeddings Of question -------------
question_embedding = embedding_model.encode(question)


# ------------- Vector Similarity Search -------------

result = collection.query(
    query_embeddings= [question_embedding],

    n_results= 3
)

# print("Result:\n", result)
# print("Result:\n", result["documents"][0])

# ------------- Generating Context -------------
context = "\n\n".join(result["documents"][0])
print("Context:\n", context)

# ------------- LLM Call -------------

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(

    base_url= "https://openrouter.ai/api/v1",

    api_key= os.getenv("OPENROUTER_API_KEY")

)

print("------------- Client is successfully connected to the OpenRouter -------------")

prompt = f"""
Answer the question ONLY USING the context provided.

context : {context}

question : {question}
"""

response = client.chat.completions.create(

    model = "openrouter/free",

    messages = [{
        "role" : "user",

        "content" : prompt
    }]
)

print("[AI] :", response.choices[0].message.content)