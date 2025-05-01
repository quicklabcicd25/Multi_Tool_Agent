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
