from resume_matchmaker_ml.extraction.schemas import CandidateProfile, JobProfile

def test_candidate_profile_defaults():
    profile = CandidateProfile()
    assert profile.skills == []
    assert profile.projects == []

def test_job_profile_defaults():
    profile = JobProfile()
    assert profile.required_skills == []
    assert profile.minimum_years_experience is None
