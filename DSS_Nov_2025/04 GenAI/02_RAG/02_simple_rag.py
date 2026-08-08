from openai import OpenAI
from dotenv import load_dotenv
import os

from pypdf import PdfReader
from pprint import pprint
import numpy as np

from sentence_transformers import SentenceTransformer

import chromadb

load_dotenv()

client = OpenAI(

    base_url="https://openrouter.ai/api/v1",

    api_key=os.getenv("OPENROUTER_API_KEY")
)

print("\nClient connected to OperRouter successfully...\n")

# ----------------------- Loading pdf -----------------------

pdf_path = "harsh.pdf"
# pdf_path = "D:\\new folder\\temp\\resume.pdf"

reader = PdfReader(stream=pdf_path)

# print("Reader:\n", reader)
# print("Pages:\n", reader.pages)

# first_page = reader.pages[0]
# print("First Page Text:\n", first_page.extract_text())

document_text = ""

for page in reader.pages:
    # document = document + page.extract_text()
    document_text += page.extract_text()

# print("Document Text:\n", document_text)

# --------------------------- Intuition of RAG ---------------------------
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

# ----------------------- Chunking -----------------------
chunk_size = 500

chunks = []

for i in range(0, len(document_text), chunk_size):
    chunk = document_text[i : i + chunk_size]
    chunks.append(chunk)

print("Number of chunks created:", len(chunks))
# print("\n\nChunks:")
# pprint(chunks)
# print(np.array(chunks))


# ----------------------- Creating Embedding Model -----------------------

embedding_model = SentenceTransformer(
    model_name_or_path= "all-MiniLM-L6-v2"
)

# ----------------------- Chroma DB -----------------------

chromadb_client = chromadb.Client()

collection = chromadb_client.create_collection(
    name= "simple_rag"
)

# ----------------------- Creating & Storing Vector Embeddings in Vector DB -----------------------

# for index, chunk in enumerate(chunks):
#     embedding = embedding_model.encode(chunk)
#     # print("embedding:\n", embedding)
#     print("\nType:", type(embedding))
#     break

for index, chunk in enumerate(chunks):
    embedding = embedding_model.encode(chunk).tolist()
    collection.add(
        ids= [str(index)],

        embeddings= [embedding],

        documents= [chunk]
    )

print("\nEmbeddings got stored successfully...\n")

# print("First embedding:")
# pprint(collection.get(ids="0"))
# pprint(collection.get(ids="0", include= ["embeddings"]))

# ----------------------- User Question -----------------------

question = input("Ask a quesion from the pdf:\n")

# ----------------------- Creating Vector Embedding Of User Question -----------------------

question_embedding = embedding_model.encode(question).tolist()

# ----------------------- Vector Similarity Search -----------------------

result = collection.query(
    query_embeddings= [question_embedding],

    n_results= 3
)

# print("Result:\n", result)
# print("Result:\n", result["documents"][0])

retrieved_text = "\n\n".join(result["documents"][0])
# print("Retrieved Text:\n", retrieved_text)

# ----------------------- LLM Call -----------------------

prompt = f"""
Answer the question ONLY using the context provided.

context: {retrieved_text}

question: {question}
"""

response = client.chat.completions.create(

    model = "deepseek/deepseek-chat",

    messages = [{
        "role" : "user",

        "content" : prompt
    }]
)

print("\nFinal answer from the AI:")
print(response.choices[0].message.content)