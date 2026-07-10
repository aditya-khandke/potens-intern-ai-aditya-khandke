# RAG Chatbot Assignment

## Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot capable of answering questions from company policy documents stored in PDF format.

The application uses semantic search with a FAISS vector database and generates responses using a local Large Language Model (LLM) running through Ollama.

---

## Features

- PDF document ingestion
- Automatic text chunking
- Embedding generation using HuggingFace models
- FAISS vector database for semantic search
- Retrieval-Augmented Generation (RAG)
- Local LLM inference using Ollama
- Source citations with file name and page number
- FastAPI backend API
- `/ask` endpoint for question answering
- `/contradict` endpoint for contradiction detection
- Streamlit frontend interface
- Offline execution without paid APIs

---

## Project Structure

```text
potens-intern-ai-aditya-khandke/
│
├── docs/                      # PDF documents
├── faiss_index/               # FAISS vector database
│
├── src/
│   ├── ingest.py              # Document ingestion and indexing
│   ├── rag.py                 # Terminal-based chatbot
│   ├── api.py                 # FastAPI backend
│   └── app.py                 # Streamlit frontend
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## Technologies Used

- Python
- LangChain
- FAISS
- HuggingFace Embeddings
- Sentence Transformers
- Ollama
- Qwen2.5
- FastAPI
- Streamlit

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd potens-intern-ai-aditya-khandke
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Local LLM Setup

Install Ollama from:

https://ollama.com/download

Download the model:

```bash
ollama pull qwen2.5:0.5b
```

Verify installation:

```bash
ollama --version
```

---

## Add Documents

Place all PDF files inside the `docs/` folder.

Example:

```text
docs/
├── Leave_Policy.pdf
├── Employee_Handbook.pdf
└── Work_From_Home_Policy.pdf
```

---

## Create Vector Database

Run the ingestion script:

```bash
python src/ingest.py
```

Expected output:

```text
Indexed 71 chunks successfully
```

---

## Running the Terminal Chatbot

Start the chatbot:

```bash
python src/rag.py
```

Example:

```text
Ask a question (or type 'exit'): What is the leave policy?
```

Example output:

```text
Answer:
The Leave Policy outlines various types of leave available, accrual mechanisms, and procedures for requesting and approving time off.

Sources:
1. File: docs\Leave_Policy.pdf
   Page: 2
```

---

## Running FastAPI Backend

Start the API server:

```bash
uvicorn src.api:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### POST `/ask`

Answers questions using the RAG pipeline.

Request:

```json
{
  "question": "What is the leave policy?"
}
```

Response:

```json
{
  "answer": "The Leave Policy outlines various types of leave available...",
  "sources": [
    {
      "file": "docs\\Leave_Policy.pdf",
      "page": 2
    }
  ]
}
```

---

### POST `/contradict`

Checks whether two statements contradict each other.

Request:

```json
{
  "statement1": "Employees can work from home two days per week.",
  "statement2": "Employees are not allowed to work from home."
}
```

Response:

```json
{
  "result": "Contradiction"
}
```

---

## Running Streamlit Frontend

Start Streamlit:

```bash
streamlit run src/app.py
```

Frontend URL:

```text
http://localhost:8501
```

The frontend sends user queries to the FastAPI `/ask` endpoint and displays answers along with source citations.

---

## Sample Questions

- What is the leave policy?
- What are the office timings?
- What is the work from home policy?
- What employee benefits are provided?
- What are the attendance rules?

---

## Git Commit History

```text
1. Initial project setup
2. Add PDF ingestion and FAISS vector indexing
3. Ignore environment files
4. Replace Gemini with local Ollama model for RAG responses
5. Add FastAPI endpoints and Streamlit interface for RAG chatbot
6. Update README with setup and usage instructions
```

---

## Author

**Aditya Khandke**

---

## Future Improvements

- Multilingual support
- Confidence score for retrieved answers
- Docker deployment
- Authentication for API endpoints
- Support for additional document formats