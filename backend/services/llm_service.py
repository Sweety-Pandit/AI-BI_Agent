from langchain_ollama import ChatOllama
from backend.config import settings


llm = ChatOllama(
    model=settings.MODEL_NAME,
    base_url=settings.OLLAMA_BASE_URL,
    temperature=0.3
)


SYSTEM_PROMPT = """
You are an AI Business Intelligence Analyst.

Analyze datasets and generate:
- trends
- risks
- recommendations
- executive summaries
- business insights
"""


def generate_ai_insights(prompt: str):

    final_prompt = f"""
    {SYSTEM_PROMPT}
    USER REQUEST:{prompt}
    """

    response = llm.invoke(final_prompt)
    return response.content