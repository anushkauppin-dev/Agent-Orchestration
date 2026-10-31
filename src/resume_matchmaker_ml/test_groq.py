from src.resume_matchmaker_ml.llm.client import (
    groq_client,
    CHAT_MODEL
)

response = groq_client.chat.completions.create(
    model=CHAT_MODEL,
    messages=[
        {
            "role": "user",
            "content": "Extract these skills into JSON: Python, SQL, Machine Learning."
        }
    ]
)

print(response.choices[0].message.content)