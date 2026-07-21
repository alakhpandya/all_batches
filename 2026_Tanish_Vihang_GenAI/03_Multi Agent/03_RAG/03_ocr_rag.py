"""
Image PDF
    ↓
OCR Extraction
    ↓
Text Cleaning
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector DB
    ↓
Retrieval of Relavant Information (RAG)
    ↓
LLM Answering
"""
from openai import OpenAI
from dotenv import load_dotenv
import os
import chromadb
from sentence_transformers import SentenceTransformer

import easyocr

load_dotenv()

client = OpenAI(

    base_url="https://openrouter.ai/api/v1",

    api_key=os.getenv("OPENROUTER_API_KEY")
)

print("\nClient connected to OperRouter successfully...\n")

# ----------------------- OCR Reader -----------------------

image_path = "mohit.jpg"

reader = easyocr.Reader(lang_list=["en"])

result = reader.readtext(image=image_path)

document_text = ""