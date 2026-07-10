# RAG Chatbot Assignment

## Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot that answers questions based on company policy documents stored in PDF format.

The chatbot:
- Loads PDF documents
- Splits documents into smaller chunks
- Creates embeddings for semantic search
- Stores embeddings in a FAISS vector database
- Retrieves relevant information based on user queries
- Generates responses using a local LLM running through Ollama

---

## Project Structure

```text
potens-intern-ai-aditya-khandke/
│
├── docs/                # PDF documents
├── faiss_index/         # FAISS vector database
├── src/
│   ├── ingest.py        # Document ingestion and indexing
│   └── rag.py           # RAG chatbot
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
Installation
Clone the Repository
git clone <repository_url>
cd potens-intern-ai-aditya-khandke
Create a Virtual Environment
python -m venv venv
Activate the Virtual Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Add Documents
Place all PDF files inside the docs/ folder.

Example:

docs/
├── Leave_Policy.pdf
├── Employee_Handbook.pdf
└── Work_From_Home_Policy.pdf
Create the Vector Database
Run the ingestion script:

python src/ingest.py
Expected output:

Indexed 71 chunks successfully
Local LLM Setup
Install Ollama:

https://ollama.com/download

Download the model:

ollama pull qwen2.5:0.5b
Install the LangChain Ollama package:

pip install langchain-ollama
Run the Chatbot
Start the chatbot:

python src/rag.py
Example:

Ask a question (or type 'exit'): What is the leave policy?
Example output:

Employees are entitled to 20 paid leaves per year.

**Technologies Used**
1.Python
2.LangChain
3.FAISS
4.Sentence Transformers
5.Ollama
6.Qwen2.5
7.HuggingFace Embeddings

**Features**
1.PDF document ingestion
2.Automatic text chunking
3.Semantic vector search
4.Retrieval-Augmented Generation (RAG)
5.Local LLM inference
6.Offline question answering
7.No API costs or usage limits

**Sample Questions**
What is the leave policy?
What are the office timings?
What is the work from home policy?
What are the employee benefits?
What are the rules regarding attendance?

**Git Commit History**
1.Initial project setup
2.Add PDF ingestion and FAISS vector indexing
3.Ignore environment files
4.Replace Gemini with local Ollama model for RAG responses

**Author**
Aditya Khandke