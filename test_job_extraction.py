
from src.resume_matchmaker_ml.extraction.llm_extractor import (
    extract_job_profile
)

sample_job_description = """
Job Title: Junior Machine Learning Engineer

Company: ABC Technologies

Requirements:
- Strong Python programming skills
- Knowledge of Machine Learning
- Experience with SQL
- Understanding of Regression and Classification
- Familiarity with Scikit-learn

Responsibilities:
- Build and evaluate machine learning models
- Clean and preprocess datasets
- Work with the data science team

Experience:
0-2 years

Education:
Bachelor's degree in Computer Science or a related field.
"""

job = extract_job_profile(sample_job_description)

print("\n--- EXTRACTED JOB PROFILE ---")
print(job.model_dump_json(indent=2))
