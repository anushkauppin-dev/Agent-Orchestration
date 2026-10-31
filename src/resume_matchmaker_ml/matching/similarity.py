
import numpy as np


def calculate_cosine_similarity(
    resume_embeddings: list[list[float]],
    job_embeddings: list[list[float]]
) -> np.ndarray:

    if not resume_embeddings or not job_embeddings:
        raise ValueError("Both embedding lists must contain vectors.")

    resume_vectors = np.asarray(resume_embeddings, dtype=np.float32)
    job_vectors = np.asarray(job_embeddings, dtype=np.float32)

    if resume_vectors.ndim != 2 or job_vectors.ndim != 2:
        raise ValueError("Embeddings must be two-dimensional arrays.")

    if resume_vectors.shape[1] != job_vectors.shape[1]:
        raise ValueError(
            "Resume and job embeddings must have the same dimensions."
        )

    resume_norms = np.linalg.norm(resume_vectors, axis=1)
    job_norms = np.linalg.norm(job_vectors, axis=1)

    if np.any(resume_norms == 0) or np.any(job_norms == 0):
        raise ValueError("Zero-length embedding vectors are not allowed.")

    # Normalize each vector
    resume_normalized = resume_vectors / resume_norms[:, np.newaxis]
    job_normalized = job_vectors / job_norms[:, np.newaxis]

    # Calculate all pairwise cosine similarities
    similarity_matrix = resume_normalized @ job_normalized.T

    return similarity_matrix
