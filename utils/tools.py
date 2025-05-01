import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
def get_tavily_tool():
    return TavilySearchResults(api_key=os.getenv("TAVILY_API_KEY"), k=5)

def get_groq_api():
    return ChatGroq(api_key=os.getenv("GROQ_API_KEY"))
