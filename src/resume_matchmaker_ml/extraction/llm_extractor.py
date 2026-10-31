import json
from ..llm.client import groq_client, CHAT_MODEL
from .schemas import CandidateProfile, JobProfile
from .prompts import CANDIDATE_SYSTEM_PROMPT, JOB_SYSTEM_PROMPT


def _client():
    return groq_client


def _extract(text: str, schema_name: str, schema: dict, system_prompt: str) -> dict:

    if not text or not text.strip():
        raise ValueError("Document text cannot be empty.")

    schema_instruction = (
        "\nReturn a JSON object matching this schema:\n"
        + json.dumps(schema)
        + "\nDo not invent information. "
        "Use null for missing optional values and empty arrays for missing lists."
    )

    response = _client().chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt + schema_instruction
            },
            {
                "role": "user",
                "content": f"Extract information from this document:\n\n{text}"
            }
        ],
        response_format={"type": "json_object"},
        temperature=0
    )

    content = response.choices[0].message.content

    if not content:
        raise ValueError("The model returned an empty response.")

    return json.loads(content)


def extract_candidate_profile(text: str) -> CandidateProfile:
    schema = CandidateProfile.model_json_schema()
    data = _extract(text, "candidate_profile", schema, CANDIDATE_SYSTEM_PROMPT)
    return CandidateProfile.model_validate(data)


def extract_job_profile(text: str) -> JobProfile:
    schema = JobProfile.model_json_schema()
    data = _extract(text, "job_profile", schema, JOB_SYSTEM_PROMPT)
    return JobProfile.model_validate(data)
