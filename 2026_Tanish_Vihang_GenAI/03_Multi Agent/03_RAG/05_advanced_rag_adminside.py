from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import easyocr
import chromadb
import os
from rank_bm25 import BM25Okapi
import numpy as np

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

# ----------------------- BM25 Setup -----------------------

# to perform keyword search, we will need words

tokenized_chunks = [ chunk.split() for chunk in chunks ]

# print("Tokenized Chunks:\n", tokenized_chunks)

bm25 = BM25Okapi(tokenized_chunks)

# ----------------------- Vector Embedding Model -----------------------
embedding_model = SentenceTransformer(
    "multi-qa-mpnet-base-cos-v1"
)
print("\nEmbedding Model Instance created\n")


# ----------------------- Vector Database - ChromaDB -----------------------
chromadb_client = chromadb.PersistentClient(path = "./chroma_storage")

collection = chromadb_client.get_or_create_collection(name = "enterprise_rag")

print("\nVector Database Created/Retrieved\n")

# ----------------------- Storing Vector Embeddings in the database -----------------------

for index, chunk in enumerate(chunks):

    embedding = embedding_model.encode(chunk).tolist()

    # print(f"Chunk-{index} is converted to vector")

    collection.upsert(

        ids= [str(index)],

        embeddings= [embedding],

        documents= [chunk],

        metadatas= [
            {
                "chunk_id" : index,

                "document" : pdf_path
            }
        ]

    )
    # print(f"Embedding of Chunk-{index} is stored into vector database")

print("\nEmbeddings are stored successfully.\n")


# ----------------------- Conversation Memory -----------------------
messages = [
    {
        "role" : "system",

        "content" : """
        You are an enterprise AI assistant.
        
        Answer the questions only from the provided context.

        If answer is not present in the context, simply return- 
        "I could not find this information in the context."
        """
    }
]


# ----------------------- Chat Loop -----------------------

print("\nEnterprise RAG started...\n")
print("Type 'exit' whenever you want to stop/quit.\n")

while True:

    question = input("[You] : ")

    if question.lower() ==  "exit":
        break

    messages.append({
        "role" : "user",

        "content" : question
    })

    # ----------------------- Semantic Search -----------------------

    question_embedding = embedding_model.encode(question).tolist()

    semantic_result = collection.query(
        query_embeddings= [question_embedding],

        n_results= 5
    )

    semantic_output = semantic_result["documents"][0]

    # ----------------------- BM25 Search (Keyword Search) -----------------------

    tokenized_question = question.split()

    bm25_output = bm25.get_top_n(
        query= tokenized_question,

        documents= chunks,

        n= 5
    )

    # print("\nBM25 Output:") 
    # print(np.array(bm25_output))

    # ----------------------- Hybrid Search -----------------------
    
    combined_output = list(
        set(semantic_output + bm25_output)
    )

    print("Number of chunks present in the combined search output =", len(combined_output))

    # ----------------------- Reranking of the chunks will come here -----------------------


    # ----------------------- Final Context -----------------------

    final_context = "\n\n".join(combined_output)

    # print("Final context:\n", final_context)

    # ----------------------- RAG Prompt -----------------------

    rag_prompt = f"""
    CONTEXT:
    {final_context}

    QUESTION:
    {question}
    """

    messages.append({
        "role" : "user",

        "content" : rag_prompt
    })

    # ----------------------- Final LLM Call -----------------------

    response = client.chat.completions.create(
    
        model = "deepseek/deepseek-chat",

        messages = messages

    )

    ai_reply = response.choices[0].message.content

    messages.append({
        "role" : "assistant",

        "content" : ai_reply
    })

    print("\n\n[Agent] :\n", ai_reply)