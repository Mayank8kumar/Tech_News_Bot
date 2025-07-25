import google.generativeai as genai
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def create_resume_vector_store(text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(text)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)

    # Overwrite previous resume index
    if os.path.exists("app/faiss_index"):
        for file in os.listdir("app/faiss_index"):
            os.remove(f"app/faiss_index/{file}")
    vector_store.save_local("app/faiss_index")
