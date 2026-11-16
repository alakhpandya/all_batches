import easyocr
from sentence_transformers import SentenceTransformer
import chromadb
from openai import OpenAI
from dotenv import load_dotenv
import os

img_path = "mohit.jpg"

reader = easyocr.Reader(lang_list=["en"])
# print("Reader:\n", reader)
print("OCR Reader object created...")


result = reader.readtext(image= img_path)
# print("Result:\n", result)
# print("No. of tuples:", len(result))
# print("First Tuple:", result[0])
# print("Second Tuple:", result[1])
# print("Third Tuple:", result[2])

print("OCR Completed successfully...")

document_text = ""
for tup in result:
    document_text = document_text + tup[1] + " "

print("Text extracted successfully...")

print("Entire text of the document:\n", document_text)

# ------------- Chunking -------------
chunk_size = 500

chunks = []

for i in range(0, len(document_text), chunk_size):
    # print(i)
    chunk = document_text[i : i+chunk_size]
    chunks.append(chunk)

# ------------- Creating Embedding Model -------------

embedding_model = SentenceTransformer(
    model_name_or_path= "all-MiniLM-L6-v2"
)

# ------------- Creating Vector Database -------------

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

print("\nEmbeddings are stored in the vector database successfully...\n")

# ------------- User's Question -------------
question = input("Ask anything from the document!\n[You] : ")


# ------------- Vector Embeddings Of question -------------
question_embedding = embedding_model.encode(question)


# ------------- Vector Similarity Search -------------

result = collection.query(
    query_embeddings= [question_embedding],

    n_results= 3
)

# ------------- Generating Context -------------
context = "\n\n".join(result["documents"][0])
print("Context:\n", context)

# ------------- LLM Call -------------

load_dotenv()

client = OpenAI(

    base_url= "https://openrouter.ai/api/v1",

    api_key= os.getenv("OPENROUTER_API_KEY")

)

print("\n------------- Client is successfully connected to the OpenRouter -------------\n")

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

print("\n[AI] :", response.choices[0].message.content)