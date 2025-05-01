from langgraph.graph import StateGraph, END
from agents.research_agent import create_research_agent
from agents.answer_agent import create_answer_agent

def build_research_workflow():
    graph = StateGraph()
    
    graph.add_node("ResearchAgent", create_research_agent())
    graph.add_node("AnswerAgent", create_answer_agent())
    
    graph.set_entry_point("ResearchAgent")
    graph.add_edge("ResearchAgent", "AnswerAgent")
    graph.add_edge("AnswerAgent", END)
    
    return graph.compile()
