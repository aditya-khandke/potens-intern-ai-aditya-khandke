import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

# Load PDFs
loader = PyPDFDirectoryLoader("docs")
documents = loader.load()


print(f"Loaded {len(documents)} documents")
# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

texts = text_splitter.split_documents(documents)
print(f"Created {len(texts)} chunks")
# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector store
vector_store = FAISS.from_documents(
    texts,
    embeddings
)

# Save locally
vector_store.save_local("faiss_index")

print(f"Indexed {len(texts)} chunks successfully!")