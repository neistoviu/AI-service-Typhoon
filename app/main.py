"""FastAPI application: routes, static files, and startup."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .knowledge import KnowledgeBase
from .chat import ChatService

# Resolve paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
STATIC_DIR = PROJECT_ROOT / "static"

# Initialize knowledge base and chat service at startup
kb = KnowledgeBase(str(PROJECT_ROOT))
chat_service = ChatService(kb)

# FastAPI app
app = FastAPI(title="Typhoon Roasters AI Service", version="0.1.0")


# --- Models ---

class ChatRequest(BaseModel):
    message: str
    mode: str = "engineer"  # "engineer" or "client"
    history: list[dict] = []


class ChatResponse(BaseModel):
    response: str
    sources: list[str] = []


# --- Routes ---

@app.get("/api/health")
async def health():
    stats = kb.get_stats()
    return {"status": "ok", "knowledge_base": stats}


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # Get relevant docs for source attribution
    relevant_docs = kb.search(request.message, top_k=5)
    sources = [doc.path for doc in relevant_docs]

    # Get response from Claude
    response_text = await chat_service.chat(
        message=request.message,
        mode=request.mode,
        history=request.history,
    )

    return ChatResponse(response=response_text, sources=sources)


@app.get("/")
async def index():
    return FileResponse(STATIC_DIR / "index.html")


# Mount static files (CSS, JS) — must be after explicit routes
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
