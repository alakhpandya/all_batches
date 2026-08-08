from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import easyocr
import chromadb
import os

load_dotenv()

client = OpenAI(

    base_url="https://openrouter.ai/api/v1",

    api_key=os.getenv("OPENROUTER_API_KEY")
)

# ---------------- LOAD PDF ----------------

pdf_path = "gk-book.pdf"

reader = PdfReader(pdf_path)

document_text = ""

for page in reader.pages:
    document_text += page.extract_text()

# OR

# image_pdf_path = "mohit.jpg"

# reader = easyocr.Reader(["en"])

# result = reader.readtext(image_pdf_path)

# document_text = ""

# for item in result:
#     # print(item)
#     # break
#     document_text = document_text + item[1] + " "


print("\nPdf loaded successfully...\n")

# ----------------------- Chunking -----------------------

chunk_size = 1000

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

# ----------------------- Conversation Memory -----------------------
messages = [
    {
        "role" : "system",

        "content" : """
        You are a helpful AI document assistant.
        
        Answer the question of the user ONLY from the context provided.

        If answer is not available in the context, just reply:
        "I could not find this information in the context"
        """
    }
]


# ----------------------- Chat Loop -----------------------
print("\nRAG Started!\n")
print("Type 'exit' whenever you want to stop.\n")

while True:
    question = input("[You] : ")

    if question.lower() ==  "exit":
        break

    messages.append({
        "role" : "user",

        "content" : question
    })

    # ----------------------- Retrieval -----------------------

    question_embedding = embedding_model.encode(question).tolist()

    result = collection.query(
        query_embeddings= [question_embedding],

        n_results= 5
    )

    retrieved_text = "\n\n".join(result["documents"][0])

    # ----------------------- Context Injection ----------------------- 

    prompt = f"""
    Answer the question ONLY from the the context provided.

    context = {retrieved_text}

    question = {question}
    """

    messages.append({
        "role" : "user",

        "content" : prompt
    })

    response = client.chat.completions.create(
    
        model = "deepseek/deepseek-chat",

        messages = messages

    )

    ai_reply = response.choices[0].message.content

    messages.append({
        "role" : "assistant",

        "content" : ai_reply
    })

    print("[Agent] :", ai_reply)