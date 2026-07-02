from sentence_transformers import SentenceTransformer
sentences = ["This is an\t\texample sentence", "Each sentence is converted"]

# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# embeddings = model.encode(sentences)
# print(embeddings)

# print(enumerate(sentences))

for x, y in enumerate(sentences):
    print(x, y)