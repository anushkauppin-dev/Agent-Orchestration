
from src.resume_matchmaker_ml.extraction.pdf_extractor import (
    extract_text_from_pdf
)

# Replace these with the actual locations of your PDF files.
resume_path = r"C:\Users\Anushka\Downloads\1901841_RESUME.pdf"
job_path = r"C:\Users\Anushka\Downloads\machine-learning-engineer-v2 job.pdf"


resume_text = extract_text_from_pdf(resume_path)
job_text = extract_text_from_pdf(job_path)

print("\n========== RESUME TEXT ==========")
print(resume_text)

print("\n========== JOB DESCRIPTION TEXT ==========")
print(job_text)
