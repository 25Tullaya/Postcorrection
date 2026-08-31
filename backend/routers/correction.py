from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/correction",
    tags=["Correction"]
)


class CorrectionRequest(BaseModel):
    text: str


class CorrectionResponse(BaseModel):
    original_text: str
    corrected_text: str


@router.post("/correct", response_model=CorrectionResponse)
def correct_text(request: CorrectionRequest):

    # ตอนนี้ยังไม่ได้เรียก mT5
    # ทำไว้สำหรับทดสอบ API ก่อน

    original = request.text

    # ตัวอย่างชั่วคราว
    corrected = original

    return {
        "original_text": original,
        "corrected_text": corrected
    }