from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(
    title="DavOps API",
    description="API de exemplo para pipeline CI/CD",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "app": "DavOps API",
        "version": "1.0.0",
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "env": os.getenv("ENV", "local")
    }

@app.get("/info")
def info():
    return {
        "app": "DavOps API",
        "env": os.getenv("ENV", "local"),
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat()
    }