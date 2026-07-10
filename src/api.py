from fastapi import FastAPI
from pydantic import BaseModel

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_classic.chains import RetrievalQA
from langchain_ollama import ChatOllama

app = FastAPI()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vector_store.as_retriever(search_kwargs={"k": 1})

llm = ChatOllama(
    model="qwen2.5:0.5b",
    num_ctx=512
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

class QuestionRequest(BaseModel):
    question: str

class ContradictRequest(BaseModel):
    statement1: str
    statement2: str    

@app.post("/ask")
def ask_question(request: QuestionRequest):
    result = qa_chain.invoke({"query": request.question})
    answer = result["result"]

    if not result["source_documents"]:
       answer = "The provided documents do not contain information about this topic."

    return {
        "answer": result["result"],
        "sources": [
            {
                "file": doc.metadata.get("source", "Unknown"),
                "page": doc.metadata.get("page", "N/A")
            }
            for doc in result["source_documents"]
        ]
    }

@app.post("/contradict")
def check_contradiction(request: ContradictRequest):

    prompt = f"""
    Determine whether these two statements contradict each other.

    Statement 1:
    {request.statement1}

    Statement 2:
    {request.statement2}

    Respond with only one of:
    - Contradiction
    - No Contradiction
    """

    response = llm.invoke(prompt)

    return {
        "result": response.content
    }