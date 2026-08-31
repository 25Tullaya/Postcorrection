from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil

router = APIRouter(
    prefix="/api/files",
    tags=["Files"]
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    allowed_extensions = [".csv", ".xlsx", ".xls"]

    file_extension = os.path.splitext(file.filename)[1].lower()

    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="รองรับเฉพาะไฟล์ CSV และ XLSX"
        )

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "status": "success",
        "message": "อัปโหลดไฟล์สำเร็จ",
        "filename": file.filename,
        "file_path": file_path
    }