from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path

from app.routes import health, analyze, classify, copilot
from app.models.database import engine, Base
from app.models.submission import Submission
from app.models.analysis import Analysis
from app.models.classification import Classification

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Cognitive Logic API",
    description="AI Governance Infrastructure",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://cognitivelogic.it", "https://api.cognitivelogic.it", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["Health"])
app.include_router(analyze.router, prefix="/api", tags=["Analysis"])
app.include_router(classify.router, prefix="/api", tags=["Classification"])
app.include_router(copilot.router, prefix="/api", tags=["Copilot"])

frontend_path = Path(__file__).parent.parent / "frontend"

@app.get("/")
async def root():
    landing_page = frontend_path / "index.html"
    if landing_page.exists():
        return FileResponse(landing_page, media_type="text/html")
    return {"message": "Cognitive Logic API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
