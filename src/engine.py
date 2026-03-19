import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from src.prompts import get_system_prompt

DB_DIR = "data/vector_store"

def get_legal_answer(query):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    
    docs = db.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    system_instructions = get_system_prompt()
    final_prompt = system_instructions.format(context=context, question=query)
    
    llm = Ollama(model="mistral") 
    
    return llm.stream(final_prompt)
