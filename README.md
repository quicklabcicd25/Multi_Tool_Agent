# Multi_Tool_Agent
# Deep Research Agent using LangGraph, LLMs, and Tools
This project demonstrates how to build a Deep Research Agent using the LangGraph framework, combining a powerful LLM (Large Language Model) with specialized tools like Tavily for search and a custom drafting tool. The aim is to create an intelligent agent that can perform multi-step research tasks: gathering information online, analyzing it, and generating professional responses.

#Architecture Overview
The system is based on a graph architecture powered by LangGraph, where each node represents a logical processing step in the research workflow. These steps include:

1. LLM-Based Decision Node (tool_calling_llm)
This node simulates calling an LLM that decides which tool to use based on the input query or message state.

2. Tool Execution Node (tools)
This node houses the actual tools the agent can use, such as:

.TavilySearchResults Tool (to search the web)

.DraftAnswer Tool (to synthesize information into a structured response)
