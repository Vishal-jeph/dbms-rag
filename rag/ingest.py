import os
from langchain_community.document_loaders import (
    PyPDFLoader,
    UnstructuredPowerPointLoader,
    Docx2txtLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_PATH = "data/"


def load_documents():
    documents = []

    for file in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, file)

        try:
            if file.endswith(".pdf"):
                loader = PyPDFLoader(path)

            elif file.endswith(".pptx"):
                loader = UnstructuredPowerPointLoader(path)

            elif file.endswith(".docx"):
                loader = Docx2txtLoader(path)

            else:
                print(f"⏭ Skipping unsupported file: {file}")
                continue

            # Load and attach metadata
            for doc in loader.load():
                doc.metadata["source"] = file
                documents.append(doc)

        except Exception as e:
            print(f"❌ Error loading {file}: {e}")

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(documents)

    # Simple cleaning
    for chunk in chunks:
        text = chunk.page_content
        text = " ".join(text.split())  # remove extra spaces/newlines
        chunk.page_content = text

    return chunks


if __name__ == "__main__":
    docs = load_documents()
    chunks = split_documents(docs)

    print(f"\n✅ Loaded {len(docs)} documents")
    print(f"✅ Created {len(chunks)} chunks")

    if chunks:
        print("\n📄 Sample chunk:\n")
        print(chunks[0].page_content)
    else:
        print("⚠️ No chunks created. Check your data folder.")