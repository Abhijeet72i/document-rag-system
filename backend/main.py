import os
import shutil
from fastapi import FastAPI, UploadFile, File
from ingest import ingest_document
from rag_pipeline import ask_question

app = FastAPI()

os.makedirs("../data", exist_ok=True)
os.makedirs("../db", exist_ok=True)


@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    path = f"../data/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks = ingest_document(path)

    return {
        "message": "Document processed",
        "chunks": chunks
    }


@app.get("/ask")
def ask(q: str):

    result = ask_question(q)

    return result