from fastapi import APIRouter, HTTPException
import os

router = APIRouter(
    prefix="/api/testing",
    tags=["Testing"]
)


@router.post("/test")
def test_model(filename: str):

    file_path = os.path.join("uploads", filename)

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="ไม่พบ Test Data"
        )

    # ตอนนี้เป็น Mock
    # ภายหลังจะเปลี่ยนเป็นผลจาก mT5 จริง

    return {
        "status": "success",
        "message": "Test Model สำเร็จ",
        "filename": filename,
        "metrics": {
            "wer": 0.1200,
            "cer": 0.0800,
            "bleu": 87.52
        }
    }