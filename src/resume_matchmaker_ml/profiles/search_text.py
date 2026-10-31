from dataclasses import dataclass
from ..extraction.schemas import CandidateProfile, JobProfile

@dataclass
class SearchSection:
    owner_id: str
    section_type: str
    text: str

def candidate_search_sections(profile: CandidateProfile, owner_id: str = "candidate") -> list[SearchSection]:
    sections = []
    if profile.professional_summary:
        sections.append(SearchSection(owner_id, "summary", profile.professional_summary))
    if profile.skills:
        skill_text = "; ".join(
            f"{s.name} ({s.evidence_type})" for s in profile.skills
        )
        sections.append(SearchSection(owner_id, "skills", skill_text))
    for i, project in enumerate(profile.projects):
        parts = [project.name or "", project.description,
                 "Technologies: " + ", ".join(project.technologies),
                 "Concepts: " + ", ".join(project.concepts),
                 "Activities: " + ", ".join(project.activities),
                 "Outcomes: " + ", ".join(project.outcomes)]
        sections.append(SearchSection(owner_id, f"project_{i}", "\n".join(p for p in parts if p.strip())))
    for i, exp in enumerate(profile.experience):
        parts = [exp.role or "", exp.organization or "", exp.description or "",
                 "Skills: " + ", ".join(exp.skills_demonstrated),
                 "Achievements: " + ", ".join(exp.achievements)]
        sections.append(SearchSection(owner_id, f"experience_{i}", "\n".join(p for p in parts if p.strip())))
    return [s for s in sections if s.text.strip()]

def job_search_sections(profile: JobProfile, owner_id: str = "job") -> list[SearchSection]:
    sections = []
    if profile.role_summary:
        sections.append(SearchSection(owner_id, "overview", profile.role_summary))
    if profile.required_skills or profile.preferred_skills:
        sections.append(SearchSection(owner_id, "skills",
            "Required: " + ", ".join(profile.required_skills) +
            "\nPreferred: " + ", ".join(profile.preferred_skills)))
    if profile.responsibilities:
        sections.append(SearchSection(owner_id, "responsibilities", "\n".join(profile.responsibilities)))
    if profile.domain_knowledge:
        sections.append(SearchSection(owner_id, "domain", ", ".join(profile.domain_knowledge)))
    return [s for s in sections if s.text.strip()]
