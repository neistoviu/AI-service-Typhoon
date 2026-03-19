"""Vercel serverless entry point — exposes the FastAPI app.

Wraps the import in try/except so that build/import failures are visible
in the HTTP response instead of silently serving the last successful deploy.
"""

import sys
import traceback
from pathlib import Path

# Ensure project root is on the Python path
_project_root = str(Path(__file__).resolve().parent.parent)
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

try:
    from app.main import app  # noqa: E402, F401
except Exception:
    # If the main app fails to import, create a minimal diagnostic app
    # so we can see the actual error in the browser.
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse

    _import_error = traceback.format_exc()

    app = FastAPI(title="Typhoon — Import Error")

    @app.get("/{path:path}")
    @app.post("/{path:path}")
    async def _fallback(path: str = ""):
        return JSONResponse(
            status_code=500,
            content={
                "status": "import_error",
                "message": "The main application failed to load. See 'traceback' for details.",
                "traceback": _import_error,
                "python_version": sys.version,
                "sys_path": sys.path[:5],
                "project_root": _project_root,
            },
        )
