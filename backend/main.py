import os
from fastapi import FastAPI, UploadFile, File
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

app = FastAPI()

# 1. Setup Models
embeddings = OllamaEmbeddings(model="llama3")
llm = OllamaLLM(model="llama3")

@app.get("/")
def home():
    return {"status": "Modern RAG API (v1.0 compatible) is Live"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not os.path.exists("data"): os.makedirs("data")
    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    loader = PyPDFLoader(file_path)
    splits = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100).split_documents(loader.load())
    
    # Store in Chroma
    Chroma.from_documents(documents=splits, embedding=embeddings, persist_directory="./chroma_db")
    return {"message": f"{file.filename} indexed."}

@app.get("/query")
async def query_pdf(question: str):
    vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    retriever = vectorstore.as_retriever()
    
    # 2. Define the Modern LCEL Pipeline (No legacy chains!)
    template = """Answer the question based only on the following context:
    {context}
    
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    
    # This is the "FAANG Style" Pipe syntax
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    response = rag_chain.invoke(question)
    return {"answer": response}
