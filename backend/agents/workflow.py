from typing import TypedDict
from langgraph.graph import StateGraph, END
from backend.services.llm_service import generate_ai_insights


class AgentState(TypedDict):
    question: str
    analysis: dict
    ai_response: str


def reasoning_node(state: AgentState):

    prompt = f"""
    Business Question:
    {state['question']}

    Analytical Results:
    {state['analysis']}

    Generate:
    - trends
    - insights
    - risks
    - recommendations
    """

    ai_response = generate_ai_insights(prompt)
    state["ai_response"] = ai_response
    return state


workflow = StateGraph(AgentState)

workflow.add_node("reasoning_node", reasoning_node)
workflow.set_entry_point("reasoning_node")
workflow.add_edge("reasoning_node",END)
graph = workflow.compile()