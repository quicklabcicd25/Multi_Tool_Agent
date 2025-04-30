
import os
from langchain_community.tools.tavily_search import TavilySearchResults

def get_tavily_tool():
    return TavilySearchResults(api_key=os.getenv("TAVILY_API_KEY"), k=5)


from langchain.agents import AgentExecutor, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
from utils.tools import get_tavily_tool

def create_research_agent():
      llm = ChatOpenAI(model="gpt-4", temperature=0)
      tavily_tool = get_tavily_tool()
    
      return AgentExecutor.from_agent_and_tools(
        agent=initialize_agent([tavily_tool], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True),
        tools=[tavily_tool],
        verbose=True
    )

#answer agent

from langchain.agents import AgentExecutor, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI

def create_answer_agent():
    llm = ChatOpenAI(model="gpt-4", temperature=0.7)
    
    return AgentExecutor.from_agent_and_tools(
        agent=initialize_agent([], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True),
        tools=[],
        verbose=True
    )

#workflow langgraph
from IPython.display import Image , display
from langgraph.graph import StateGraph, START, END
from agents.research_agent import create_research_agent
from agents.answer_agent import create_answer_agent

def build_research_workflow():
    
    input = "query"
    output = "response"
    graph = StateGraph(input=input, output=output)
    graph.add_node("ResearchAgent", create_research_agent())
    graph.add_node("AnswerAgent", create_answer_agent())
     
    graph.set_entry_point("ResearchAgent")
    graph.add_edge("ResearchAgent", "AnswerAgent")
    graph.add_edge("AnswerAgent", END)
    graph = build_research_workflow()
    print(graph)
    return graph


#main.py

import os
from dotenv import load_dotenv
from workflows.research_flow import build_research_workflow

load_dotenv()

if __name__ == "__main__":
    graph = build_research_workflow()
    query = input("what are the AI trends in education")
    result = graph.invoke(query)
    
    
    print("\n✅ Final Answer:\n")
    print(result)
