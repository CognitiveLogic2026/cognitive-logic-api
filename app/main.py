from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI(
    title="Cognitive Logic API",
    description="AI Governance Infrastructure",
    version="1.0.0",
)

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "Cognitive Logic API v1.0",
        "version": "1.0.0"
    }

@app.get("/status")
async def status():
    return {
        "status": "operational",
        "brains": {"brain_a": "Claude", "brain_b": "Gemini"}
    }

@app.get("/")
async def root():
    return {"message": "Cognitive Logic API - Visit /docs for API documentation"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
