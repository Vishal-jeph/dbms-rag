# 📚 AI-Powered DBMS Assistant (RAG आधारित Chatbot)

An intelligent, domain-specific chatbot built using **Retrieval-Augmented Generation (RAG)** to answer Database Management System (DBMS) queries based on custom course materials.

---

## 🚀 Live Demo
👉 [https://your-app-name.streamlit.app](https://dbms-rag-kiit.streamlit.app/)

---

## 🧠 Problem Statement

Traditional LLMs often generate **hallucinated or generic answers** when asked domain-specific academic questions.

This project solves that by:
- Grounding responses in **actual course content**
- Providing **context-aware, accurate answers**
- Enabling **automated student doubt resolution**

---

## ⚙️ Architecture Overview

User Query  
→ Embedding Generation  
→ FAISS Vector Search (Top-K Retrieval)  
→ Context Injection  
→ LLM (Groq - LLaMA 3.1)  
→ Final Answer + Source Attribution  

---

## 🔥 Key Features

- 📄 Supports **multi-format documents** (PDF, PPT, DOCX)  
- 🧠 Uses **semantic search (FAISS + MiniLM embeddings)**  
- 🎯 Context-aware answers using **RAG pipeline**  
- 💬 Interactive **Streamlit chat interface**  
- 📚 Provides **source references for transparency**  
- ⚡ Fast inference using **Groq LLM API**

---

## 🛠️ Tech Stack

- **Language:** Python  
- **LLM:** Groq (LLaMA 3.1)  
- **Embeddings:** HuggingFace (MiniLM)  
- **Vector DB:** FAISS  
- **Framework:** LangChain  
- **Frontend:** Streamlit  
- **Deployment:** Streamlit Cloud  

---

## 📊 Data Processing

- Processed **300+ document chunks** from DBMS course material  
- Applied **recursive chunking strategy** for optimal retrieval  
- Attached metadata for **source tracking**

---

## 🧪 Example Queries

- What is normalization?  
- Explain B+ Trees  
- Difference between primary and secondary index  
- What is transaction management in DBMS?  

---

## ⚡ How It Works

1. Documents are loaded and split into chunks  
2. Each chunk is converted into embeddings  
3. Stored in FAISS vector database  
4. User query is embedded and matched with relevant chunks  
5. Retrieved context is passed to LLM for answer generation  

---

## 🏗️ Project Structure

dbms-rag/
│
├── app/ # Streamlit frontend
├── rag/ # Core RAG pipeline
│ ├── ingest.py
│ ├── retriever.py
│ └── generator.py
│
├── vectorstore/ # FAISS index
├── data/ # Course materials
├── requirements.txt
└── README.md


---

## 🚀 Setup Instructions

### 1. Clone Repo
```bash
git clone [https://github.com/your-username/dbms-rag.git](https://github.com/Vishal-jeph/dbms-rag)
cd dbms-rag

to install Dependencies pip install -r requirements.txt

setup evn - GROQ_API_KEY=your_api_key_here

to run - streamlit run app/main.py


