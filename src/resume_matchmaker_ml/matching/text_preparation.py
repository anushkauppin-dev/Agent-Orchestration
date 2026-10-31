
from ..extraction.schemas import CandidateProfile, JobProfile


def prepare_candidate_texts(
    profile: CandidateProfile
) -> list[str]:
    """Convert candidate profile information into meaningful text chunks."""

    chunks = []

    # 1. Skills
    for skill in profile.skills:
        text = f"Skill: {skill.name}"

        if skill.category:
            text += f". Category: {skill.category}"

        for evidence in skill.evidence:
            text += f". Evidence: {evidence.statement}"

        chunks.append(text)

    # 2. Work experience
    for experience in profile.experience:
        parts = [
            experience.role,
            experience.organization,
            experience.description
        ]

        parts.extend(experience.skills_demonstrated)
        parts.extend(experience.achievements)

        text = ". ".join(part for part in parts if part)

        if text:
            chunks.append(f"Experience: {text}")

    # 3. Projects
    for project in profile.projects:
        parts = [project.name, project.description]

        parts.extend(project.technologies)
        parts.extend(project.concepts)
        parts.extend(project.activities)
        parts.extend(project.outcomes)

        parts.extend(
            evidence.statement
            for evidence in project.evidence
        )

        text = ". ".join(part for part in parts if part)

        if text:
            chunks.append(f"Project: {text}")

    # 4. Education
    for education in profile.education:
        parts = [
            education.qualification,
            education.field_of_study,
            education.institution
        ]

        text = ". ".join(part for part in parts if part)

        if text:
            chunks.append(f"Education: {text}")

    return chunks


def prepare_job_requirements(
    profile: JobProfile
) -> list[str]:
    """Convert job profile into individual requirements."""

    requirements = []

    if profile.role_summary:
        requirements.append(
            f"Role summary: {profile.role_summary}"
        )

    for skill in profile.required_skills:
        requirements.append(f"Required skill: {skill}")

    for skill in profile.preferred_skills:
        requirements.append(f"Preferred skill: {skill}")

    for responsibility in profile.responsibilities:
        requirements.append(f"Responsibility: {responsibility}")

    for domain in profile.domain_knowledge:
        requirements.append(f"Domain knowledge: {domain}")

    return requirements
