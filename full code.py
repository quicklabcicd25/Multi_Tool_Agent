import os
from langchain_community.tools.tavily_search import TavilySearchResults
#from langchain_groq import ChatGroq

def get_tavily_tool():
    return TavilySearchResults(api_key=os.getenv("TAVILY_API_KEY"), k=5)

#impoort os
from dotenv import load_dotenv
load_dotenv()
import os
os.environ["TAVILY_API_KEY"]="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"
os.environ["GROQ_API_KEY"]="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"

#initialize llm model
from langchain_groq import ChatGroq

llm=ChatGroq(model="llama3-70b-8192")

from langchain.prompts import PromptTemplate     #GIVING ANSWER and drafting OF QUERY
from langchain_groq import ChatGroq
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
import os


# Set API key
os.environ["GROQ_API_KEY"] = "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" 

# Step 1: Create the chain function

def create_drafting_agent():
    llm = ChatGroq(model="llama3-70b-8192", temperature=0.3)
    prompt = PromptTemplate(
        input_variables=["research_content"],
        template="""
You are an expert AI assistant.
Using the following research content, draft a structured, clear, and professional answer:

Research Content:
{research_content}

Write the final answer now.
"""
    )
    return prompt | llm

# Step 2: Define the callable function for the tool

def draft_answer_fn(research_content: str) -> str:
    chain = create_drafting_agent()
    return chain.invoke({"research_content": research_content})

# Step 3: Wrap it as a LangChain Tool
draft_tool = Tool(
    name="DraftAnswer",
    func=draft_answer_fn,
    descriptdraft_answeion="Use this to draft a professional answer from given research content"
)


# #research agent
from langchain.agents import AgentExecutor, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_groq import ChatGroq
#from langchain_openai import ChatOpenAI
from utils.tools import get_tavily_tool

def create_research_agent():
      llm =ChatGroq(model="llama3-70b-8192", temperature=0)
      tavily_tool = get_tavily_tool()
    
      return AgentExecutor.from_agent_and_tools(
        agent=initialize_agent([tavily_tool], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True),
        tools=[tavily_tool],
        verbose=True
    )



##Step 4: Use it in an agent
#tools = [ create_research_agent,draft_answer_tool]

#agent = initialize_agent(
 #   tools=tools,
  #  llm=ChatGroq(model="llama3-70b-8192"),
   # agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    #verbose=True
#)

#3 Example usage
#agent.invoke("Draft an answer using the following research content: The rise of AI in education is reshaping personalized learning and automation.")
