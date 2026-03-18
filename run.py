#!/usr/bin/env python3
"""Typhoon Roasters AI Service — entry point."""

import os
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("ANTHROPIC_API_KEY"):
    print("\n  ERROR: ANTHROPIC_API_KEY not set.")
    print("  Copy .env.example to .env and add your key:")
    print("    cp .env.example .env")
    print("    # Edit .env with your Anthropic API key\n")
    raise SystemExit(1)

import uvicorn

if __name__ == "__main__":
    print("\n  Typhoon Roasters AI Service")
    print("  http://localhost:8000\n")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
