from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb
from openai import OpenAI
from dotenv import load_dotenv
import os

pdf_path = "gk-book.pdf"

reader = PdfReader(stream=pdf_path)
print("Pypdf object created...")

document_text = ""
for page in reader.pages:
    # document_text = document_text + page.extract_text()
    document_text += page.extract_text()

print("Text extracted successfully...")

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

# ------------- Conversation Memory -------------
messages = [
    {
        "role" : "system",
        "content" : """
        You are a helpful AI document assitant. 

        Answer the user's question ONLY from the provided context. If answer is not available in the context, simply say: "I could not find the answer in the document(s)."
        """
    }
]

# ------------- OpenAI Agent -------------
load_dotenv()

client = OpenAI(

    base_url= "https://openrouter.ai/api/v1",

    api_key= os.getenv("OPENROUTER_API_KEY")

)

# ------------- Chat Loop -------------
while True:
    # ------------- User's Question -------------
    question = input('Ask anything from the document, or enter "quit" to exit...\n[You] : ')

    if question.lower() == "quit":
        break

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

    messages.append({
        "role" : "user",

        "content" : f"""
        question : {question}

        context : {context}
        """
    })

    # ------------- LLM Call -------------
    response = client.chat.completions.create(
        model = "openrouter/free",

        messages = messages
    )

    ai_response = response.choices[0].message.content
    messages.append({
        "role" : "assistant",

        "content" : ai_response
    })

    print("[AI Agent]:\n", ai_response, "\n")