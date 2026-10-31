
import json
from pathlib import Path


def save_embeddings(
    chunks: list[str],
    embeddings: list[list[float]],
    document_id: str,
    document_type: str,
    output_dir: str = "data/embeddings"
) -> str:

    if len(chunks) != len(embeddings):
        raise ValueError(
            "Number of chunks and embeddings must be equal."
        )

    if document_type not in {"resume", "job_description"}:
        raise ValueError(
            "document_type must be 'resume' or 'job_description'."
        )

    if not document_id or Path(document_id).name != document_id:
        raise ValueError("document_id must be a simple filename-safe ID.")

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    records = []

    for index, (chunk, embedding) in enumerate(
        zip(chunks, embeddings)
    ):
        records.append({
            "document_id": document_id,
            "document_type": document_type,
            "chunk_index": index,
            "text": chunk,
            "embedding": embedding,
            "embedding_model": "intfloat/e5-base-v2",
            "embedding_dimensions": len(embedding)
        })

    file_path = output_path / f"{document_id}.json"

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=4)

    return str(file_path)
