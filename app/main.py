"""FastAPI application: routes, static files, and startup."""

from __future__ import annotations

import traceback
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from typing import List, Dict

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
    history: List[Dict] = []


class ChatResponse(BaseModel):
    response: str
    sources: List[str] = []


# --- Routes ---

@app.get("/api/health")
async def health():
    stats = kb.get_stats()
    return {"status": "ok", "knowledge_base": stats}


@app.post("/api/chat")
async def chat(request: ChatRequest):
    try:
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

    except Exception as e:
        error_detail = f"{type(e).__name__}: {str(e)}"
        print(f"[CHAT ERROR] {error_detail}")
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"detail": error_detail},
        )


@app.get("/")
async def index():
    return FileResponse(STATIC_DIR / "index.html")


# Mount static files (CSS, JS) — must be after explicit routes
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
