from sentence_transformers import SentenceTransformer


# Load the embedding model once when the application starts
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text: str):
    """
    Convert text into a 384-dimensional embedding vector.
    """

    embedding = model.encode(text)

    return embedding.tolist()