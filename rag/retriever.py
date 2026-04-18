import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from rag.ingest import load_documents, split_documents

DB_PATH = "vectorstore/"


def create_vectorstore():
    print("🔄 Loading documents...")
    documents = load_documents()

    print("🔄 Splitting documents...")
    chunks = split_documents(documents)

    print("🔄 Creating embeddings...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("🔄 Building FAISS index...")

    vectorstore = FAISS.from_documents(chunks, embeddings)

    vectorstore.save_local(DB_PATH)

    print(f"✅ Vectorstore saved at {DB_PATH}")


def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)

    return vectorstore


def get_retriever():
    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 5   # top 5 relevant chunks
        }
    )

    return retriever


if __name__ == "__main__":
    create_vectorstore()