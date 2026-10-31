import math

def precision_at_k(relevant: set[str], ranked: list[str], k: int = 5) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    return sum(1 for item in ranked[:k] if item in relevant) / k

def recall_at_k(relevant: set[str], ranked: list[str], k: int = 5) -> float:
    if not relevant:
        return 0.0
    return sum(1 for item in ranked[:k] if item in relevant) / len(relevant)

def ndcg_at_k(relevant: set[str], ranked: list[str], k: int = 5) -> float:
    dcg = sum((1 / math.log2(i + 2)) for i, item in enumerate(ranked[:k]) if item in relevant)
    ideal_hits = min(len(relevant), k)
    idcg = sum(1 / math.log2(i + 2) for i in range(ideal_hits))
    return dcg / idcg if idcg else 0.0
