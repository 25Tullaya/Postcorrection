from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.correction import router as correction_router
from routers.files import router as files_router
from routers.training import router as training_router
from routers.testing import router as testing_router


app = FastAPI(
    title="Thai Text Post-Correction API",
    description="API สำหรับระบบแก้ไขคำผิดภาษาไทย",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(correction_router)
app.include_router(files_router)
app.include_router(training_router)
app.include_router(testing_router)


@app.get("/")
def root():
    return {
        "message": "Thai Text Post-Correction API",
        "status": "running"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "success",
        "message": "Backend is working"
    }