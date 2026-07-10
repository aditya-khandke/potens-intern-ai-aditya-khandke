# RAG Chatbot with Citations

## Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot capable of answering questions from multiple PDF documents using semantic search and a local Large Language Model (LLM).

The system ingests PDF documents, splits them into chunks, creates embeddings, stores them in a FAISS vector database, retrieves relevant information based on user queries, and generates answers with citations.

The project also provides:
- A FastAPI backend with REST endpoints
- A Streamlit frontend interface
- Citation support
- Contradiction checking between statements
- Offline inference using a local LLM

---

## Features

- PDF document ingestion
- Text chunking and embedding generation
- FAISS vector database
- Retrieval-Augmented Generation (RAG)
- Source citations with file name and page number
- FastAPI backend
- `/ask` endpoint
- `/contradict` endpoint
- Streamlit frontend
- Local LLM inference using Ollama
- Offline execution without paid APIs

---

## Project Structure

```text
potens-intern-ai-aditya-khandke/
│
├── docs/
│   ├── Leave_Policy.pdf
│   ├── Employee_Handbook.pdf
│   └── ...
│
├── faiss_index/
│
├── src/
│   ├── ingest.py
│   ├── rag.py
│   ├── api.py
│   └── app.py
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

```text
https://ollama.com/download
```

Pull the model:

```bash
ollama pull qwen2.5:0.5b
```

Verify installation:

```bash
ollama list
```

---

## Adding Documents

Place all PDF files inside the `docs` folder.

Example:

```text
docs/
├── Leave_Policy.pdf
├── Employee_Handbook.pdf
├── Work_From_Home_Policy.pdf
└── Benefits_Policy.pdf
```

---

## Chunking Strategy

Documents are split into smaller overlapping chunks before embedding generation.

- Chunk Size: **500 characters**
- Chunk Overlap: **50 characters**

The overlap preserves context between adjacent chunks and improves retrieval quality for questions spanning multiple sections of a document.

---

## Creating the Vector Database

Run:

```bash
python src/ingest.py
```

Example output:

```text
Indexed 71 chunks successfully
```

---

## Running Terminal Chatbot

Run:

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

Start backend server:

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

Answers user questions using RAG retrieval.

#### Request

```json
{
  "question": "What is the leave policy?"
}
```

#### Response

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

#### Request

```json
{
  "statement1": "Employees can work from home two days per week.",
  "statement2": "Employees are not allowed to work from home."
}
```

#### Response

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

The frontend sends requests to the FastAPI backend and displays answers along with citations.

---

## Sample Questions

- What is the leave policy?
- What are the office timings?
- What is the work from home policy?
- What employee benefits are provided?
- What are the attendance rules?

---

## Design Decisions

- FAISS was selected for fast local vector search.
- HuggingFace Embeddings were used to avoid external API costs.
- Ollama + Qwen2.5 were selected to allow completely offline inference.
- FastAPI was chosen for lightweight API development.
- Streamlit was used for rapid UI development.

---

## Handling Hallucinations

The system avoids unsupported answers by checking retrieved documents before generating responses.

If no relevant context is found, the application returns:

```text
The provided documents do not contain information about this topic.
```

instead of generating a fabricated answer.

---

## Limitations

- Multilingual retrieval quality depends on embedding performance.
- Contradiction detection currently compares statements using the LLM and does not perform document-level reasoning.
- Large models may require additional RAM.

---

## Future Improvements

- Better multilingual retrieval
- Confidence scores for answers
- Re-ranking layer
- Docker deployment
- Authentication for API endpoints
- Support for additional document formats

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

## AI Usage Log

| Tool | Approximate Usage | Purpose |
|------|------------------|---------|
| ChatGPT | ~200 messages | Debugging, architecture guidance, FastAPI integration, Streamlit integration, README generation |
| Gemini | ~20 messages | Generating required Pdfs |

---

## Author

**Aditya Khandke**