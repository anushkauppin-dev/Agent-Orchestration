from src.resume_matchmaker_ml.llm.client import groq_client

models = groq_client.models.list()

for model in models.data:
    print(model.id)