
import json
from pathlib import Path

from resume_matchmaker_ml.matching.similarity import (
    calculate_cosine_similarity
)


# Load saved embedding JSON files
resume_path = Path("data/embeddings/candidate_001.json")
job_path = Path("data/embeddings/job_junior_python_developer.json")

with resume_path.open("r", encoding="utf-8") as file:
    resume_records = json.load(file)

with job_path.open("r", encoding="utf-8") as file:
    job_records = json.load(file)


# Extract embedding vectors
resume_embeddings = [
    record["embedding"] for record in resume_records
]

job_embeddings = [
    record["embedding"] for record in job_records
]


# Calculate similarity
similarity_matrix = calculate_cosine_similarity(
    resume_embeddings,
    job_embeddings
)


# Display results
print("\nRESUME-JOB SIMILARITY MATRIX")
print("--------------------------------")

print("Rows: Resume chunks")
print("Columns: Job description chunks")

print(similarity_matrix)

print("\nMATRIX DIMENSIONS:", similarity_matrix.shape)

assert similarity_matrix.shape == (
    len(resume_embeddings),
    len(job_embeddings)
)

assert (similarity_matrix >= -1.0001).all()
assert (similarity_matrix <= 1.0001).all()

print("\nCosine similarity calculation successful!")
