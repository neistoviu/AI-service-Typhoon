"""Chat logic: builds prompts with knowledge context and calls OpenAI API."""

from __future__ import annotations

import os
from typing import Optional, List

from openai import AsyncOpenAI

from .knowledge import KnowledgeBase, Document
from .prompts import get_system_prompt


class ChatService:
    MODEL = os.environ.get("OPENAI_MODEL", "gpt-5.4")
    MAX_TOKENS = 4096

    def __init__(self, kb: KnowledgeBase):
        self.kb = kb
        self.api_key = os.environ.get("OPENAI_API_KEY")
        self.client = AsyncOpenAI(api_key=self.api_key) if self.api_key else None
        self.reasoning_effort = os.environ.get("OPENAI_REASONING_EFFORT", "medium")

    async def chat(
        self,
        message: str,
        mode: str = "engineer",
        history: Optional[List[dict]] = None,
    ) -> str:
        """Process a chat message and return the model response."""
        if self.client is None:
            raise RuntimeError("OPENAI_API_KEY is not set")

        # Search knowledge base for relevant documents
        relevant_docs = self.kb.search(message, top_k=5)

        # Build the context block from relevant documents
        context_block = self._build_context(relevant_docs)

        # Build system prompt
        system_prompt = get_system_prompt(mode)
        system_with_context = f"{system_prompt}\n\n---\n\n## Knowledge Base Context\n\nBelow are the most relevant documents from the Typhoon Roasters service knowledge base. Use them to answer the user's question.\n\n{context_block}"

        # Build OpenAI input messages
        input_messages = [{"role": "system", "content": system_with_context}]
        if history:
            for msg in history[-10:]:  # Keep last 10 messages for context
                input_messages.append({
                    "role": msg["role"],
                    "content": msg["content"],
                })
        input_messages.append({"role": "user", "content": message})

        response = await self.client.responses.create(
            model=self.MODEL,
            input=input_messages,
            max_output_tokens=self.MAX_TOKENS,
            reasoning={"effort": self.reasoning_effort},
        )

        return self._extract_text(response)

    def _build_context(self, docs: list[Document]) -> str:
        """Build a formatted context string from retrieved documents."""
        if not docs:
            return "(No relevant documents found in the knowledge base.)"

        parts = []
        for doc in docs:
            parts.append(
                f"### [{doc.category}] {doc.path}\n"
                f"**Title:** {doc.title}\n\n"
                f"{doc.content}\n"
            )
        return "\n---\n\n".join(parts)

    def _extract_text(self, response) -> str:
        """Extract text from OpenAI Responses API output."""
        if getattr(response, "output_text", None):
            return response.output_text

        parts: list[str] = []
        for item in getattr(response, "output", []) or []:
            for content in getattr(item, "content", []) or []:
                if getattr(content, "type", None) == "output_text" and getattr(content, "text", None):
                    parts.append(content.text)

        if parts:
            return "\n".join(parts)

        raise ValueError("OpenAI response did not contain text output")
