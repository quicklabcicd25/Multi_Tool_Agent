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
