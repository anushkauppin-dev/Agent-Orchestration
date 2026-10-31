# ML architecture notes

## Candidate path
Resume -> text extraction -> candidate schema extraction -> profile sections ->
embeddings -> hybrid retrieval against job sections.

## Employer path
Job document -> text extraction -> job schema extraction -> job sections ->
embeddings -> hybrid retrieval against candidate sections.

## Matching principles
1. Use structured filters for hard requirements only when the employer explicitly marks them mandatory.
2. Use vector retrieval to find semantic equivalents.
3. Use keyword retrieval to retain exact skill/tool matches
4. Rerank only the retrieved shortlist if evaluation shows a measurable gain.
5. Return evidence explaining each match and each gap.
6. Never interpret similarity as hiring probability.

## Production considerations
- Add OCR for image-only PDFs.
- Add chunk/section IDs and document version IDs to stored vectors.
- Reprocess embeddings when the embedding model or dimensions change.
- Add rate limits, retries, timeouts, token limits and cost tracking around provider calls.
- Redact or minimize personal information before embedding; identity fields are not useful semantic signals.
- Use consented/anonymized data for evaluation.
