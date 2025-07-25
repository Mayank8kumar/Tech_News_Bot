from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.extract_text import extract_text_from_pdf
from app.services.vector_store import create_resume_vector_store

router = APIRouter()

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    contents = await file.read()

    try:
        # Save to temp and re-open as PyPDF2 needs a file-like object
        with open("temp_resume.pdf", "wb") as f:
            f.write(contents)
        with open("temp_resume.pdf", "rb") as f:
            text = extract_text_from_pdf(f)
        create_resume_vector_store(text)
        return {"message": "Resume processed and stored successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
