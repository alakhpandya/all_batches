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

# ---------------- EMBEDDING MODEL ----------------

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# ---------------- VECTOR DATABASE ----------------

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(
    name="conversation_rag"
)

# ---------------- STORE EMBEDDINGS ----------------

for index, chunk in enumerate(chunks):

    embedding = embedding_model.encode(chunk).tolist()

    collection.add(

        ids=[str(index)],

        embeddings=[embedding],

        documents=[chunk]
    )

print("\nEmbeddings Stored Successfully!")

# ---------------- CONVERSATION MEMORY ----------------

messages = [

    {
        "role": "system",
        "content": """
        You are a helpful AI document assistant.

        Answer questions ONLY from the provided document context.

        If answer is not available in context,
        say:
        'I could not find this information in the document.'
        """
    }
]

# ---------------- CHAT LOOP ----------------

print("\nConversational RAG Started!")
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

    # ---------------- RETRIEVAL ----------------

    question_embedding = embedding_model.encode(question).tolist()

    results = collection.query(

        query_embeddings=[question_embedding],

        n_results=5
    )

    retrieved_text = "\n".join(results["documents"][0])

    # ---------------- CONTEXT INJECTION ----------------

    rag_prompt = f"""

    DOCUMENT CONTEXT:
    {retrieved_text}

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