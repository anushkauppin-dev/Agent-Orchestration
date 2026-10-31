
import json
from pathlib import Path

from resume_matchmaker_ml.matching.requirement_matcher import (
    match_requirement
)


# Load saved resume data
resume_path = Path("data/embeddings/candidate_001.json")

with resume_path.open("r", encoding="utf-8") as file:
    resume_records = json.load(file)


# Extract original chunks and their embeddings
resume_chunks = [
    record["text"] for record in resume_records
]

resume_embeddings = [
    record["embedding"] for record in resume_records
]


# Temporary example requirements for testing
job_requirements = [
    "Python programming",
    "SQL database management",
    "Machine learning",
    "FastAPI backend development"
]


# Match each requirement against the resume
for requirement in job_requirements:

    result = match_requirement(
        requirement=requirement,
        resume_chunks=resume_chunks,
        resume_embeddings=resume_embeddings
    )

    print("\n-----------------------------------")
    print("JOB REQUIREMENT:", result["requirement"])
    print("BEST MATCHING RESUME CHUNK:")
    print(result["best_matching_chunk"])
    print("SIMILARITY SCORE:", round(result["similarity_score"], 4))
    print("RESUME CHUNK INDEX:", result["resume_chunk_index"])
