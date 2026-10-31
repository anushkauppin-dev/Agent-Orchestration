
from src.resume_matchmaker_ml.extraction.llm_extractor import (
    extract_candidate_profile
)

sample_resume = """
Ananya Sharma
Email: ananya@example.com

Skills: Python, SQL, Machine Learning

Experience:
Data Analyst Intern at ABC Technologies (2024-2025).
Worked with Python and SQL to analyze datasets.

Projects:
Sales Prediction using Machine Learning.
Built a regression model using Python and Scikit-learn.

Education:
B.Tech in Computer Science.
"""

profile = extract_candidate_profile(sample_resume)

print("\n--- EXTRACTED CANDIDATE PROFILE ---")
print(profile.model_dump_json(indent=2))
