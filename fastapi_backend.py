from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
import shutil
import os
from pathlib import Path
from models.extract_text import extract_text

app = FastAPI()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "message": "PDF uploaded successfully"}

@app.get("/extract_text/")
def extract_text_from_pdf(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    text = extract_text(file_path)
    return {"filename": filename, "extracted_text": text[:1000]}  # Limit output size

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
