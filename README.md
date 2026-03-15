# ⚖️ Nyaya-LLM: Offline Legal Assistant

**Built for FOSS Hack 2026**

Nyaya-LLM is a privacy-first, fully offline Retrieval-Augmented Generation (RAG) system designed to help citizens, legal professionals, and cyber investigators query the **Bhartiya Nyaya Sanhita (BNS) 2023**. 

By running entirely on local hardware without internet dependencies, Nyaya-LLM ensures absolute data privacy and zero API costs, making it a secure tool for sensitive legal and investigative environments.

---

## ✨ Key Features
* **100% Offline & Private:** No data is ever sent to the cloud. All document processing, vector storage, and LLM inference happen locally on your machine.
* **Accurate Legal Retrieval:** Uses ChromaDB to search the official BNS 2023 documentation, ensuring the AI grounds its answers in actual law rather than hallucinating.
* **Multilingual Support:** Capable of understanding and responding to legal queries in both English and Tamil.
* **Accessible UI:** Clean, intuitive chat interface powered by Streamlit.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **LLM Engine:** Ollama (Mistral 7B)
* **RAG Framework:** LangChain
* **Vector Database:** ChromaDB
* **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)
* **Frontend:** Streamlit

---

## 🚀 Quick Start Guide

### 1. Prerequisites
You must have [Python](https://www.python.org/downloads/) and [Ollama](https://ollama.com/) installed on your system. 

Before running the application, download the required local LLM via your terminal:
```bash
ollama pull mistral
