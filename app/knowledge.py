"""Knowledge base loader and search engine for Typhoon Roasters service docs."""

from __future__ import annotations

import os
import re
import math
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class Document:
    path: str
    filename: str
    category: str  # troubleshooting, manuals, models, standard_procedures
    title: str
    headings: list[str]
    content: str
    tokens: list[str] = field(default_factory=list)


class KnowledgeBase:
    # Directories to index (relative to project root)
    KNOWLEDGE_DIRS = ["troubleshooting", "manuals", "models", "standard_procedures"]

    # Component/symptom keywords for boosting
    COMPONENT_KEYWORDS = {
        "heater", "heaters", "нагреватель", "нагреватели", "тэн",
        "sensor", "sensors", "датчик", "датчики", "термопара",
        "motor", "мотор", "двигатель",
        "vfd", "частотник", "инвертор",
        "smoke", "дым",
        "seal", "seals", "уплотнитель", "уплотнение",
        "rcd", "узо", "дифавтомат",
        "actuator", "актуатор", "заслонка",
        "airflow", "воздушный", "поток",
        "electrical", "электрика", "проводка",
        "impeller", "крыльчатка",
        "cyclone", "циклон",
        "filter", "фильтр",
        "software", "софт", "программа", "по",
        "cooling", "охлаждение",
        "glass", "стекло", "свет",
        "destoner", "дестонер",
        "temperature", "температура",
    }

    MODEL_KEYWORDS = {
        "2.5": ["2.5kg", "2.5", "2,5"],
        "5": ["5kg", "5 kg"],
        "10": ["10kg", "10 kg"],
        "20": ["20kg", "20 kg"],
        "25": ["25kg", "25 kg"],
        "30": ["30kg", "30 kg"],
        "gas": ["gas", "газ"],
        "electro": ["electro", "electric", "электро", "электрический"],
    }

    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.documents: list[Document] = []
        self.idf: dict[str, float] = {}
        self._load()
        self._build_idf()

    def _load(self):
        """Load all markdown files from knowledge directories."""
        for dir_name in self.KNOWLEDGE_DIRS:
            dir_path = self.base_path / dir_name
            if not dir_path.exists():
                continue
            for md_file in sorted(dir_path.glob("*.md")):
                content = md_file.read_text(encoding="utf-8")
                title = self._extract_title(content)
                headings = self._extract_headings(content)
                tokens = self._tokenize(f"{title} {' '.join(headings)} {content}")

                self.documents.append(Document(
                    path=str(md_file.relative_to(self.base_path)),
                    filename=md_file.name,
                    category=dir_name,
                    title=title,
                    headings=headings,
                    content=content,
                    tokens=tokens,
                ))

    def _extract_title(self, content: str) -> str:
        match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        return match.group(1).strip() if match else ""

    def _extract_headings(self, content: str) -> list[str]:
        return [m.group(1).strip() for m in re.finditer(r"^#{1,3}\s+(.+)$", content, re.MULTILINE)]

    def _tokenize(self, text: str) -> list[str]:
        text = text.lower()
        text = re.sub(r"[^\w\s\.\-/]", " ", text)
        return [t for t in text.split() if len(t) > 1]

    def _build_idf(self):
        """Build inverse document frequency for all tokens."""
        n = len(self.documents)
        if n == 0:
            return
        doc_freq: dict[str, int] = {}
        for doc in self.documents:
            unique_tokens = set(doc.tokens)
            for token in unique_tokens:
                doc_freq[token] = doc_freq.get(token, 0) + 1
        self.idf = {
            token: math.log(n / df)
            for token, df in doc_freq.items()
        }

    def search(self, query: str, top_k: int = 5) -> list[Document]:
        """Search knowledge base by query, return top_k most relevant documents."""
        query_tokens = self._tokenize(query)
        if not query_tokens:
            return self.documents[:top_k]

        scores: list[tuple[float, int]] = []

        for idx, doc in enumerate(self.documents):
            score = self._score_document(doc, query_tokens, query.lower())
            scores.append((score, idx))

        scores.sort(key=lambda x: x[0], reverse=True)
        return [self.documents[idx] for score, idx in scores[:top_k] if score > 0]

    def _score_document(self, doc: Document, query_tokens: list[str], query_lower: str) -> float:
        """Score a document against query tokens using TF-IDF + bonuses."""
        score = 0.0
        doc_token_counts: dict[str, int] = {}
        for t in doc.tokens:
            doc_token_counts[t] = doc_token_counts.get(t, 0) + 1
        doc_len = max(len(doc.tokens), 1)

        # TF-IDF score
        for qt in query_tokens:
            tf = doc_token_counts.get(qt, 0) / doc_len
            idf = self.idf.get(qt, 0)
            score += tf * idf

        # Bonus: title/heading match
        title_lower = doc.title.lower()
        headings_lower = " ".join(doc.headings).lower()
        for qt in query_tokens:
            if qt in title_lower:
                score += 2.0
            if qt in headings_lower:
                score += 1.0

        # Bonus: component keyword match
        for qt in query_tokens:
            if qt in self.COMPONENT_KEYWORDS:
                if qt in doc.content.lower():
                    score += 1.5

        # Bonus: model keyword match
        for model, aliases in self.MODEL_KEYWORDS.items():
            if any(alias in query_lower for alias in aliases):
                if any(alias in doc.content.lower() for alias in aliases):
                    score += 1.0

        # Bonus: category relevance
        if "процедур" in query_lower or "procedure" in query_lower or "как проверить" in query_lower:
            if doc.category == "standard_procedures":
                score += 2.0
        if "модел" in query_lower or "model" in query_lower or "спецификац" in query_lower:
            if doc.category == "models":
                score += 2.0

        return score

    def get_all_categories(self) -> dict[str, int]:
        """Return count of documents per category."""
        cats: dict[str, int] = {}
        for doc in self.documents:
            cats[doc.category] = cats.get(doc.category, 0) + 1
        return cats

    def get_stats(self) -> dict:
        """Return knowledge base statistics."""
        total_lines = sum(doc.content.count("\n") for doc in self.documents)
        return {
            "total_documents": len(self.documents),
            "total_lines": total_lines,
            "categories": self.get_all_categories(),
        }
