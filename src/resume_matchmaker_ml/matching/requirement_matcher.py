
import numpy as np

from resume_matchmaker_ml.data.embeddings.embedder import generate_embeddings
from resume_matchmaker_ml.matching.similarity import calculate_cosine_similarity


def match_requirement(
    requirement: str,
    resume_chunks: list[str],
    resume_embeddings: list[list[float]]
) -> dict:

    if not requirement or not requirement.strip():
        raise ValueError("Requirement cannot be empty.")

    if not resume_chunks:
        raise ValueError("Resume chunks cannot be empty.")

    if len(resume_chunks) != len(resume_embeddings):
        raise ValueError(
            "Resume chunks and embeddings must have equal lengths."
        )

    # Convert the individual job requirement into an embedding
    requirement_embedding = generate_embeddings(
        [requirement],
        is_query=True
    )

    # Compare the requirement against every resume chunk
    similarity_matrix = calculate_cosine_similarity(
        resume_embeddings,
        requirement_embedding
    )

    # Find the most similar resume chunk
    best_index = int(np.argmax(similarity_matrix[:, 0]))

    best_score = float(similarity_matrix[best_index, 0])

    return {
        "requirement": requirement,
        "best_matching_chunk": resume_chunks[best_index],
        "similarity_score": best_score,
        "resume_chunk_index": best_index
    }
