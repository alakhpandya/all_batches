from openai import OpenAI
from dotenv import load_dotenv
import os

from pypdf import PdfReader


load_dotenv()

client = OpenAI(

    base_url="https://openrouter.ai/api/v1",

    api_key=os.getenv("OPENROUTER_API_KEY")
)

print("\nClient connected to OperRouter successfully...\n")

# ----------------------- Loading pdf -----------------------

# pdf_path = "D:\\new_folder\\Ritu_Kathiria_Resume.pdf"
pdf_path = "Ritu_Kathiria_Resume.pdf"

reader = PdfReader(stream=pdf_path)

# print("Reader object:", reader)
# print("\nPages list:", reader.pages)
# print("\nFirst page object:\n", reader.pages[0])
# print("\nText in the page:\n", reader.pages[0].extract_text())

document_text = ""

for page in reader.pages:
    document_text += page.extract_text()

print("\nPDF loaded successfully...\n")
# print("Document text:\n", document_text)


# --------------------------- Intuition of RAG ---------------------------
"""
Steps:
- We will break down the document in small parts ("chunks")
- We can choose any size of each of this chunks depending on our document length. Typically for bigger documents we keep it either 500 characters or 1000 characters
- We create vector embedding for each of these chunks
- Then we will ask user for any question from the document
- We will also create vector embedding for that question
- And finally we will retrieve 3 or 5 or 10 chunks which are nearest to the vector embedding of the question
- This group of chunks (converted into a single string) will act as context for our LLM
"""

# ----------------------- Chunking -----------------------

chunk_size = 100

chunks = []

# st = "Hello, how are you?"
# st[2 : 10]
# st[ : len(st) : 5]
# st[0 : chunk_size]

for i in range(0, len(document_text), chunk_size):          # i = 0, 50, 100, 150, 200, ...
    chunk = document_text[i : i+chunk_size]
    chunks.append(chunk)

print(f"\nTotal chunks created = {len(chunks)}\n")
print("\nChunks:\n", chunks)