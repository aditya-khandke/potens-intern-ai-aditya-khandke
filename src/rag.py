from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_classic.chains import RetrievalQA
from langchain_ollama import ChatOllama

load_dotenv()

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS index
vector_store = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# Create retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 1})

# Load Gemini model
llm = ChatOllama(
    model="qwen2.5:0.5b",
    num_ctx=512

)

# Create RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)


# Ask questions
# Ask questions
while True:
    question = input("\nAsk a question (or type 'exit'): ")

    if question.lower() == "exit":
        break

    result = qa_chain.invoke({"query": question})

    answer = result["result"]
    sources = result["source_documents"]

    print("\nAnswer:")
    print(answer)

    print("\nSources:")
    for i, doc in enumerate(sources, 1):
        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", "N/A")

        print(f"{i}. File: {source}")
        print(f"   Page: {page}")
        print(f"   Snippet: {doc.page_content[:150]}...")
        print()