import json

from src.resume_matchmaker_ml.extraction.pdf_extractor import (
    extract_text_from_pdf
)
from src.resume_matchmaker_ml.extraction.llm_extractor import (
    extract_candidate_profile,
    extract_job_profile
)
from src.resume_matchmaker_ml.matching.text_preparation import (
    prepare_candidate_texts,
    prepare_job_requirements
)

resume_path = r"C:\Users\Anushka\OneDrive\Documents\Sample_Candidate_Resume.docx"
job_path = r"C:\Users\Anushka\OneDrive\Documents\Employer_Job_Description_Junior_Python_Developer.docx"
resume_text = extract_text_from_pdf(resume_path)
job_text = extract_text_from_pdf(job_path)

candidate = extract_candidate_profile(resume_text)
job = extract_job_profile(job_text)

candidate_chunks = prepare_candidate_texts(candidate)
job_requirements = prepare_job_requirements(job)

print("\n===== CANDIDATE JSON =====")
print(json.dumps(
    candidate.model_dump(mode="json"),
    indent=4
))

print("\n===== JOB JSON =====")
print(json.dumps(
    job.model_dump(mode="json"),
    indent=4
))

# Step 4: Prepare text chunks for embeddings
candidate_chunks = prepare_candidate_texts(candidate)
job_requirements = prepare_job_requirements(job)

print("\nCandidate chunks:", len(candidate_chunks))
print("Job requirements:", len(job_requirements))