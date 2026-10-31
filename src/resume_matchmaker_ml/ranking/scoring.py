from dataclasses import dataclass

@dataclass
class MatchBreakdown:
    total_score: float
    skill_coverage: float
    project_relevance: float
    experience_relevance: float
    notes: list[str]

def _coverage(required: list[str], candidate_terms: list[str]) -> float:
    if not required:
        return 1.0
    available = {x.casefold() for x in candidate_terms}
    hits = sum(1 for item in required if item.casefold() in available)
    return hits / len(required)

def score_candidate_for_job(required_skills: list[str],
                            candidate_skills: list[str],
                            project_relevance: float,
                            experience_relevance: float) -> MatchBreakdown:
    """Transparent baseline score; weights are starting hypotheses, not truth."""
    skill = _coverage(required_skills, candidate_skills)
    project = max(0.0, min(1.0, project_relevance))
    experience = max(0.0, min(1.0, experience_relevance))
    total = 100 * (0.40 * skill + 0.35 * project + 0.25 * experience)
    notes = []
    if skill < 1:
        notes.append("Some required skills were not found explicitly.")
    if project < 0.5:
        notes.append("Limited project evidence for this role.")
    return MatchBreakdown(round(total, 2), round(skill, 3),
                          round(project, 3), round(experience, 3), notes)
