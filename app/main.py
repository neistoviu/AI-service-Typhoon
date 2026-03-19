"""FastAPI application: routes, static files, and startup."""

from __future__ import annotations

import os
import sys
import traceback
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from typing import List, Dict, Optional

# Resolve paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
STATIC_DIR = PROJECT_ROOT / "static"

# FastAPI app — created FIRST, before any heavy imports
app = FastAPI(title="Typhoon Roasters AI Service", version="0.2.0")

# Try to initialize knowledge base and chat service.
# If it fails (e.g. missing files on Vercel), we still have the app object
# and diagnostic endpoints will show the error.
_init_error: Optional[str] = None
kb = None
chat_service = None

try:
    from .knowledge import KnowledgeBase
    from .chat import ChatService

    kb = KnowledgeBase(str(PROJECT_ROOT))
    chat_service = ChatService(kb)
except Exception:
    _init_error = traceback.format_exc()


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
    result = {
        "status": "ok" if _init_error is None else "init_error",
        "version": "0.2.0",
        "python_version": sys.version,
        "project_root": str(PROJECT_ROOT),
        "static_dir_exists": STATIC_DIR.exists(),
    }

    if _init_error:
        result["init_error"] = _init_error
        return result

    # Knowledge base stats
    try:
        result["knowledge_base"] = kb.get_stats()
    except Exception as e:
        result["knowledge_base_error"] = str(e)

    # API key status
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    result["api_key_status"] = f"set ({len(key)} chars)" if len(key) > 10 else "NOT SET"
    result["model"] = chat_service.MODEL

    # Test Claude API connectivity
    try:
        response = await chat_service.client.messages.create(
            model=chat_service.MODEL,
            max_tokens=20,
            messages=[{"role": "user", "content": "Say OK"}],
        )
        result["api_test"] = f"ok: {response.content[0].text}"
    except Exception as e:
        result["api_test"] = f"error: {type(e).__name__}: {str(e)}"

    return result


@app.post("/api/chat")
async def chat(request: ChatRequest):
    if _init_error or chat_service is None:
        return JSONResponse(
            status_code=503,
            content={
                "detail": "Service not initialized",
                "init_error": _init_error or "unknown",
            },
        )

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
    html_path = STATIC_DIR / "index.html"
    if html_path.exists():
        return FileResponse(html_path)
    return JSONResponse(
        content={
            "error": "index.html not found",
            "static_dir": str(STATIC_DIR),
            "static_exists": STATIC_DIR.exists(),
            "project_root": str(PROJECT_ROOT),
            "files_in_root": [f.name for f in PROJECT_ROOT.iterdir()][:20] if PROJECT_ROOT.exists() else [],
        }
    )


# Mount static files (CSS, JS) — must be after explicit routes
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
