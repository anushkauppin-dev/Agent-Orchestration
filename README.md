# Resume Matchmaker – ML / AI Module

A provider-agnostic ML layer for a resume-to-job matchmaking prototype. This repository focuses on document understanding, structured extraction, embeddings, hybrid retrieval, ranking, and evaluation—not API/backend infrastructure.

## Pipeline

1. Extract text from PDF/DOCX (`document/`).
2. Convert resume and job-description text into validated Pydantic schemas (`extraction/`).
3. Normalize profiles into searchable text sections (`profiles/`).
4. Generate pretrained embeddings through a provider adapter (`embeddings/`).
5. Retrieve candidates/jobs using vector similarity plus keyword overlap (`retrieval/`).
6. Rank results with an explainable, configurable score (`ranking/`).
7. Evaluate retrieval/ranking against a small human-labelled dataset (`evaluation/`).

## Important design choices

- No model training or fine-tuning is required.
- LLM extraction and embedding providers are replaceable.
- The LLM must not invent missing facts. Missing values remain `null` or empty lists.
- Preserve evidence/source snippets for extracted skills where possible.
- Treat listed skills separately from skills demonstrated in projects/work.
- Embeddings are model-specific. Re-embed all records if the embedding model changes.
- Similarity scores are relevance signals, not probabilities of hiring success.
- Human review should be available before a profile is used for matching.

## Quick start

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
```

Add an API key to `.env` if using OpenAI. Do not commit `.env`.

### Extract text

```python
from pathlib import Path
from src.resume_matchmaker_ml.document.extractors import extract_text

text = extract_text(Path("samples/resume.pdf"))
print(text)
```

### Extract a candidate profile

```python
from src.resume_matchmaker_ml.extraction.llm_extractor import extract_candidate_profile
from src.resume_matchmaker_ml.extraction.schemas import CandidateProfile

profile: CandidateProfile = extract_candidate_profile(text)
print(profile.model_dump_json(indent=2))
```

### Create profile sections for embeddings

```python
from src.resume_matchmaker_ml.profiles.search_text import candidate_search_sections
sections = candidate_search_sections(profile)
```

### Generate embeddings

```python
from src.resume_matchmaker_ml.embeddings.factory import get_embedding_provider
provider = get_embedding_provider()
vectors = provider.embed_texts([section.text for section in sections])
```

### Match a job against candidates

The retrieval and ranking modules are storage-agnostic. Supply candidate/job sections and vectors loaded from your chosen storage layer. See `examples/demo_matching.py`.

## Supported inputs

- PDF: PyMuPDF text extraction.
- DOCX: python-docx text extraction.
- Scanned/image-only PDF: OCR adapter stub in `document/ocr.py`; configure Tesseract separately.

## Provider configuration

The default adapters use OpenAI APIs:
- Extraction: a configurable chat model with JSON-schema output.
- Embeddings: a configurable embedding model.

Set `LLM_PROVIDER` and `EMBEDDING_PROVIDER` in `.env`. The current implementation includes OpenAI adapters and clear interfaces for adding Gemini, Claude, or local Sentence Transformers.

## Evaluation before deployment

Use a manually labelled dataset of real or consented/anonymized resumes and job descriptions. Compare:
- keyword-only retrieval,
- embedding-only retrieval,
- hybrid retrieval,
- hybrid retrieval + reranking (optional future extension).

Track Precision@K, Recall@K and nDCG@K. Do not tune weights on the same examples used for final evaluation.

## Scope deliberately excluded

FastAPI routes, authentication, PostgreSQL models, file upload endpoints, frontend, and deployment infrastructure are excluded because this package is the ML/AI layer only.
