import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from backend.config import settings


VECTOR_DB_PATH = settings.VECTOR_DB_PATH

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_vector_store(text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    chunks = splitter.split_text(text)
    documents = [
        Document(page_content=chunk)
        for chunk in chunks
    ]

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=VECTOR_DB_PATH
    )

    vector_store.persist()
    return len(chunks)


def retrieve_context(query: str):
    if not os.path.exists(VECTOR_DB_PATH):
        return []

    vector_store = Chroma(persist_directory=VECTOR_DB_PATH, embedding_function=embedding_model)

    results = vector_store.similarity_search(query, k=3)

    return [
        result.page_content
        for result in results
    ]