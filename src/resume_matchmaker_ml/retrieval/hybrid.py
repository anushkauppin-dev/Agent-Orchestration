from dataclasses import dataclass
from collections import Counter
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

@dataclass
class SearchDocument:
    entity_id: str
    section_type: str
    text: str
    embedding: list[float]

@dataclass
class RetrievalResult:
    entity_id: str
    vector_score: float
    keyword_score: float
    hybrid_score: float
    matched_terms: list[str]

def _terms(text: str) -> set[str]:
    return {w.lower().strip(".,;:!?()[]{}") for w in text.split() if len(w) > 1}

def hybrid_retrieve(query: str, query_embedding: list[float],
                    documents: list[SearchDocument],
                    vector_weight: float = 0.7,
                    keyword_weight: float = 0.3,
                    top_k: int = 20) -> list[RetrievalResult]:
    """Simple in-memory hybrid retrieval baseline.

    For production scale, move vector and full-text retrieval into PostgreSQL
    with pgvector and tsvector; keep this function as a testable baseline.
    """
    if not documents:
        return []
    q = np.asarray(query_embedding, dtype=float).reshape(1, -1)
    matrix = np.asarray([d.embedding for d in documents], dtype=float)
    vector_scores = cosine_similarity(q, matrix)[0]
    query_terms = _terms(query)
    results = []
    for doc, vscore in zip(documents, vector_scores):
        doc_terms = _terms(doc.text)
        matched = sorted(query_terms & doc_terms)
        keyword_score = len(matched) / max(len(query_terms), 1)
        hybrid = vector_weight * float(vscore) + keyword_weight * keyword_score
        results.append((doc.entity_id, float(vscore), keyword_score, hybrid, matched))
    # Collapse multiple sections belonging to the same entity using max score.
    best = {}
    for row in results:
        if row[0] not in best or row[3] > best[row[0]][3]:
            best[row[0]] = row
    ranked = sorted(best.values(), key=lambda x: x[3], reverse=True)[:top_k]
    return [RetrievalResult(*r) for r in ranked]
