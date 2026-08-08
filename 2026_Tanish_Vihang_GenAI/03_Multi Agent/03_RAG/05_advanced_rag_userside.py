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


# ----------------------- Vector Embedding Model -----------------------
embedding_model = SentenceTransformer(
    "multi-qa-mpnet-base-cos-v1"
)
print("\nEmbedding Model Instance created\n")


# ----------------------- Vector Database - ChromaDB -----------------------
chromadb_client = chromadb.PersistentClient(path = "./chroma_storage")

collection = chromadb_client.get_collection(name = "enterprise_rag")

print("\nVector Database Retrieved\n")


# ----------------------- Retrieving Chunks From ChromaDB -----------------------

print(collection)