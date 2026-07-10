from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import easyocr
import chromadb
import os
from rank_bm25 import BM25Okapi

load_dotenv()

client = OpenAI(

    base_url="https://openrouter.ai/api/v1",

    api_key=os.getenv("OPENROUTER_API_KEY")
)

# ---------------- LOAD PDF ----------------


pdf_path = "gk-book.pdf"
# pdf_path = "harsh.pdf"

reader = PdfReader(pdf_path)

document_text = ""

for page in reader.pages:

    extracted = page.extract_text()

    if extracted:
        document_text += extracted

print("\nPDF Loaded Successfully!")

# OR

# image_pdf_path = "mohit.jpg"

# reader = easyocr.Reader(["en"])

# result = reader.readtext(image_pdf_path)

# document_text = ""

# for item in result:
#     # print(item)
#     # break
#     document_text = document_text + item[1] + " "

# print("\nOCR Text\n")
# print(document_text)


# ---------------- CHUNKING ----------------

chunk_size = 500

chunks = [

    document_text[i:i + chunk_size]

    for i in range(0, len(document_text), chunk_size)
]

print(f"Total Chunks: {len(chunks)}")

# ---------------- BM25 Setup ----------------

tokenized_chunks = []
for chunk in chunks:
    tokenized_chunks.append(chunk.split())

bm25 = BM25Okapi(tokenized_chunks)


# ---------------- EMBEDDING MODEL ----------------

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# ---------------- Persistent ChromaDB ----------------

chroma_client = chromadb.PersistentClient(path="./chroma_storage")

collection = chroma_client.get_or_create_collection(
    name = "enterprise_rag"
)

# ---------------- STORE EMBEDDINGS ----------------

for index, chunk in enumerate(chunks):

    embedding = embedding_model.encode(chunk).tolist()

    collection.upsert(

        ids=[str(index)],

        embeddings=[embedding],

        documents=[chunk],

        metadatas=[
            {
                "chunk_id" : index
            }
        ]
    )

print("\nEmbeddings Stored Successfully!")

# ---------------- CONVERSATION MEMORY ----------------

messages = [

    {
        "role": "system",
        "content": """
        You are an enterprise AI assistant.

        Answer questions ONLY from the provided document context.

        If answer is not available in context,
        say:
        'I could not find this information in the document.'
        """
    }
]

# ---------------- CHAT LOOP ----------------

print("\Enterpise RAG Started!")
print("Type 'exit' to stop.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    # Store user message
    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # ---------------- Semantic Search ----------------

    question_embedding = embedding_model.encode(question).tolist()

    semantic_results = collection.query(

        query_embeddings=[question_embedding],

        n_results=5
    )

    # print(semantic_results)
    semantic_chunks = semantic_results["documents"][0]
    # print(semantic_chunks, "\n\n")

    # ---------------- BM25 (Keyword) Search ----------------

    tokenized_query = question.split()

    bm25_result = bm25.get_top_n(
        query= tokenized_query,

        documents= chunks,

        n= 3
    )

    # print(bm25_result)
    # ---------------- Hybrid Search ----------------

    combined_chunks = list(
     
        set(semantic_chunks + bm25_result)
    
    )

    # print(combined_chunks)

    # ---------------- Reranking of the chunks will come here ----------------

    # ---------------- Final Context ----------------

    final_context = "\n".join(combined_chunks)

    # print("\n:Retrieved Context:\n\n", final_context)

    # ---------------- RAG Prompt ----------------

    rag_prompt = f"""

    DOCUMENT CONTEXT:
    {final_context}

    USER QUESTION:
    {question}

    """

    # Add retrieved context
    messages.append(
        {
            "role": "system",
            "content": rag_prompt
        }
    )

    # ---------------- LLM CALL ----------------

    response = client.chat.completions.create(

        model="deepseek/deepseek-chat",

        messages=messages,

        # max_tokens=200,

        temperature=0.7
    )

    ai_reply = response.choices[0].message.content

    print("\nAI:", ai_reply, "\n")

    # Store assistant response
    messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )