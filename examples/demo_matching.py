"""Illustrative retrieval demo; replace vectors with embeddings from your provider."""
from resume_matchmaker_ml.retrieval.hybrid import SearchDocument, hybrid_retrieve

# Toy vectors are only for demonstrating the function interface.
query = "Python backend API development"
query_vector = [1.0, 0.0, 0.0]
docs = [
    SearchDocument("candidate_1", "project", "Built Python REST API using FastAPI", [0.95, 0.1, 0.0]),
    SearchDocument("candidate_2", "project", "Designed marketing campaigns and content", [0.0, 0.9, 0.1]),
]
for result in hybrid_retrieve(query, query_vector, docs):
    print(result)
