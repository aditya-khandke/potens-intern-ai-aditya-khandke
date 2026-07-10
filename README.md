# RAG Chatbot with Citations

## Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot capable of answering questions from PDF documents using semantic search and a local Large Language Model (LLM).

The system ingests PDF documents, splits them into chunks, creates embeddings, stores them in a FAISS vector database, retrieves relevant information based on user queries, and generates answers with citations.

The project provides:

- FastAPI backend with REST APIs
- Streamlit frontend interface
- Source citations
- Contradiction detection
- Local LLM inference using Ollama
- Hallucination reduction using strict context-based prompting

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
- Hallucination handling for unsupported queries

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

Install Ollama:

```text
https://ollama.com/download
```

Download the model:

```bash
ollama pull qwen2.5:0.5b
```

Verify installation:

```bash
ollama list
```

---

## Adding Documents

Place all PDF files inside the `docs` directory.

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

Documents are divided into overlapping chunks before embedding generation.

- Chunk Size: **500 characters**
- Chunk Overlap: **50 characters**

The overlap preserves context between neighboring chunks and improves retrieval quality for questions that span multiple sections of a document.

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

## Running the Terminal Chatbot

Run:

```bash
python src/rag.py
```

Example:

```text
Ask a question (or type 'exit'): What is the leave policy?
```

Example response:

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

Answers user questions using document retrieval and RAG.

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

The frontend sends requests to the FastAPI backend and displays answers with citations.

---

## Sample Questions

- What is the leave policy?
- What are the office timings?
- What is the work from home policy?
- What employee benefits are provided?
- What are the attendance rules?

---

## Design Decisions

- **FAISS** was selected for efficient local vector search.
- **HuggingFace Embeddings** were used to avoid paid APIs.
- **Ollama + Qwen2.5** were chosen for completely offline inference.
- **FastAPI** was selected for lightweight API development.
- **Streamlit** was used for rapid frontend development.

---

## Handling Hallucinations

The chatbot answers questions only using retrieved document context.

A custom prompt instructs the model to avoid generating unsupported information.

If no relevant information is found in the knowledge base, the system returns:

```text
The provided documents do not contain information about this topic.
```

instead of generating fabricated answers.

---

## Limitations

- Multilingual retrieval quality depends on embedding model performance.
- Contradiction detection currently relies on LLM reasoning and not document-grounded verification.
- Larger local models may require additional memory resources.

---

## Future Improvements

- Better multilingual retrieval
- Confidence scoring for answers
- Retrieval re-ranking
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
7. Improve hallucination handling in RAG pipeline
```

---

## AI Usage Log

| Tool | Approximate Usage | Purpose |
|------|-------------------|---------|
| ChatGPT | ~200 messages | Debugging, architecture guidance, FastAPI integration, Streamlit integration, hallucination handling improvements, and README generation |
| Gemini | ~20 messages | Generating required Pdfs |

---

## Note

The project originally used the Gemini API for response generation. However, due to API quota limitations and to ensure completely offline and reproducible execution, the implementation was migrated to Ollama with the Qwen2.5 model running locally.

This eliminates dependency on external APIs and avoids rate limits or API key exhaustion issues.

---

## Author

**Aditya Khandke**