from fastapi import FastAPI
from api.auth import router as auth_router

app = FastAPI(
    title="Enterprise Backend System",
    description="Production-ready backend API with high scalability and performance.",
    version="1.0.0"
)

app.include_router(auth_router, prefix="/api", tags=["Authentication"])

@app.get("/", tags=["Root"])
def root():
    return {
        "status": "running",
        "project": "enterprise backend system",
        "author": "Majid Al-Sakni",
        "message": "Welcome to the Enterprise Backend API"
    }
