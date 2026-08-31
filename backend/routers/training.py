from fastapi import APIRouter, HTTPException
import os

router = APIRouter(
    prefix="/api/training",
    tags=["Training"]
)


@router.post("/train")
def train_model(filename: str):

    file_path = os.path.join("uploads", filename)

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="ไม่พบ Training Data"
        )

    # ตอนนี้ยังไม่ใช้ mT5
    # เป็นการจำลองการ Train เพื่อทดสอบระบบ

    return {
        "status": "success",
        "message": "Train Model สำเร็จ",
        "filename": filename,
        "model_status": "trained"
    }