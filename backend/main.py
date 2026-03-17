from fastapi import FastAPI, UploadFile, File
import os
from .rag_logic import RAGAssistant

app = FastAPI()
assistant = RAGAssistant()

@app.get("/")
def home():
    return {"status": "Research Assistant API is Live"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not os.path.exists("data"): os.makedirs("data")
    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    assistant.ingest_pdf(file_path)
    return {"message": f"{file.filename} indexed successfully."}

@app.get("/query")
async def query_pdf(question: str):
    answer = assistant.ask(question)
    return {"answer": answer}

