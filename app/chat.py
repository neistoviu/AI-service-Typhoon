"""Chat logic: builds prompts with knowledge context and calls Claude API."""

from __future__ import annotations

from typing import Optional, List

import anthropic

from .knowledge import KnowledgeBase, Document
from .prompts import get_system_prompt


class ChatService:
    MODEL = "claude-sonnet-4-20250514"
    MAX_TOKENS = 4096

    def __init__(self, kb: KnowledgeBase):
        self.kb = kb
        self.client = anthropic.AsyncAnthropic()

    async def chat(
        self,
        message: str,
        mode: str = "engineer",
        history: Optional[List[dict]] = None,
    ) -> str:
        """Process a chat message and return Claude's response."""
        # Search knowledge base for relevant documents
        relevant_docs = self.kb.search(message, top_k=5)

        # Build the context block from relevant documents
        context_block = self._build_context(relevant_docs)

        # Build system prompt
        system_prompt = get_system_prompt(mode)
        system_with_context = f"{system_prompt}\n\n---\n\n## Knowledge Base Context\n\nBelow are the most relevant documents from the Typhoon Roasters service knowledge base. Use them to answer the user's question.\n\n{context_block}"

        # Build messages
        messages = []
        if history:
            for msg in history[-10:]:  # Keep last 10 messages for context
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"],
                })
        messages.append({"role": "user", "content": message})

        # Call Claude API (async)
        response = await self.client.messages.create(
            model=self.MODEL,
            max_tokens=self.MAX_TOKENS,
            system=system_with_context,
            messages=messages,
        )

        return response.content[0].text

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
