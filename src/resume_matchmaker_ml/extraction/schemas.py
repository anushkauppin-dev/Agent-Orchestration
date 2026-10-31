from typing import Literal
from pydantic import BaseModel, Field, EmailStr, ConfigDict

class Evidence(BaseModel):
    statement: str
    source_text: str | None = None
    source_section: Literal["skills", "experience", "project", "education", "other"] = "other"

class Project(BaseModel):
    name: str | None = None
    description: str
    technologies: list[str] = Field(default_factory=list)
    concepts: list[str] = Field(default_factory=list)
    activities: list[str] = Field(default_factory=list)
    outcomes: list[str] = Field(default_factory=list)
    evidence: list[Evidence] = Field(default_factory=list)

class Experience(BaseModel):
    role: str | None = None
    organization: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    description: str | None = None
    skills_demonstrated: list[str] = Field(default_factory=list)
    achievements: list[str] = Field(default_factory=list)

class Education(BaseModel):
    qualification: str | None = None
    institution: str | None = None
    field_of_study: str | None = None
    start_date: str | None = None
    end_date: str | None = None

class Skill(BaseModel):
    name: str
    category: str | None = None
    evidence_type: Literal["listed", "demonstrated", "inferred"] = "listed"
    evidence: list[Evidence] = Field(default_factory=list)

class CandidateProfile(BaseModel):
    model_config = ConfigDict(extra="forbid")
    full_name: str | None = None
    email: str | None = None
    phone: str | None = None
    location: str | None = None
    professional_summary: str | None = None
    skills: list[Skill] = Field(default_factory=list)
    experience: list[Experience] = Field(default_factory=list)
    projects: list[Project] = Field(default_factory=list)
    education: list[Education] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list)
    career_interests: list[str] = Field(default_factory=list)
    years_experience: float | None = None

class JobProfile(BaseModel):
    model_config = ConfigDict(extra="forbid")
    job_title: str | None = None
    company: str | None = None
    role_summary: str | None = None
    required_skills: list[str] = Field(default_factory=list)
    preferred_skills: list[str] = Field(default_factory=list)
    responsibilities: list[str] = Field(default_factory=list)
    domain_knowledge: list[str] = Field(default_factory=list)
    minimum_years_experience: float | None = None
    education_requirements: list[str] = Field(default_factory=list)
    location: str | None = None
    work_mode: str | None = None
    employment_type: str | None = None
