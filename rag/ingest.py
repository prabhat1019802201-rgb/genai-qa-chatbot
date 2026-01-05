from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings


def ingest_pdfs(pdf_paths, provider: str, api_key: str | None):
    documents = []

    for path in pdf_paths:
        loader = PyPDFLoader(path)
        documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    # -------------------------------
    # Embeddings Selection
    # -------------------------------
    if provider == "OpenAI":
        embeddings = OpenAIEmbeddings(api_key=api_key)
    else:
        # Hugging Face embeddings (used for HF + Groq)
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore
