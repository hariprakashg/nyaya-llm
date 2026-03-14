import os
os.environ["ANONYMIZED_TELEMETRY"] = "False"
import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

PDF_FILE = "data/raw_documents/Bhartiya_Nyaya_Sanhita_2023.pdf"
DB_PATH = "data/vector_store"

def initialize_brain():
    print(" Loading embedding model (all-MiniLM-L6-v2)...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    print(f" Reading Legal Document: {PDF_FILE}")
    loader = PyPDFLoader(PDF_FILE)
    documents = loader.load()
    
    print(" Splitting into manageable chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    text_chunks = splitter.split_documents(documents)
    
    print(f" Saving {len(text_chunks)} sections to local database...")
    vector_db = Chroma.from_documents(
        documents=text_chunks, 
        embedding=embeddings, 
        persist_directory=DB_PATH
    )
    vector_db.persist()
    print(" Offline brain built successfully!")

if __name__ == "__main__":
    if not os.path.exists(PDF_FILE):
        print(f" Error: Could not find {PDF_FILE}. Did you rename the download?")
    else:
        initialize_brain()
