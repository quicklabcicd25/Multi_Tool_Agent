# Multi_Tool_Agent
# Deep Research Agent using LangGraph, LLMs, and Tools
This project demonstrates how to build a Deep Research Agent using the LangGraph framework, combining a powerful LLM (Large Language Model) with specialized tools like Tavily for search and a custom drafting tool. The aim is to create an intelligent agent that can perform multi-step research tasks: gathering information online, analyzing it, and generating professional responses.

#Architecture Overview
The system is based on a graph architecture powered by LangGraph, where each node represents a logical processing step in the research workflow. These steps include:

1. LLM-Based Decision Node (tool_calling_llm)
This node simulates calling an LLM that decides which tool to use based on the input query or message state.

2. Tool Execution Node (tools)
This node houses the actual tools the agent can use, such as:

TavilySearchResults Tool (to search the web)

DraftAnswer Tool (to synthesize information into a structured response)

#Key Components and Implementation
1. Prompt + LLM for Drafting
The draft_answer_fn is a Python function wrapped in a Tool. It uses a structured prompt template combined with ChatGroq's Llama 3-70B model to generate high-quality professional responses. Here’s how:


 prompt = PromptTemplate(
    input_variables=["research_content"],
    template="""
You are an expert AI assistant...
"""
)
chain = prompt | ChatGroq(...)


2. Connecting LLMs to Tools with ToolNode
LangGraph's ToolNode allows us to plug in tools as functional nodes in the graph. Each tool is defined using the Tool class from LangChain. To connect them:
used conditional edges so that the LLM node (tool_calling_llm) decides which path the graph should take next.
3. Tavily Tool for Web Search (Optional Extension)
Although not added in the working graph above, you can easily add Tavily with:
Then, include it in ToolNode([...]) alongside the drafting tool. Tavily handles the real-time web search part of the agent.

How the Graph Works
The graph is built using StateGraph, where a State is passed between nodes. The steps flow like this:

Input query starts at START

tool_calling_llm simulates a decision process (which could later be replaced with an actual LLM)

Based on simple logic (e.g., always use tools), it routes to the tools node

The tool executes and the graph ends at END

Visualizing the Graph:
You can visualize the graph structure using:
This helps debug and understand the sequence of operations clearly.

























Conclusion:
This Deep Research Agent is modular, extensible, and intelligent. By combining LLMs, tools like Tavily, and LangGraph’s node-based orchestration, you create a robust pipeline capable of tackling real-world information gathering and synthesis tasks in a highly scalable and transparent way.

Let me know if you want this formatted as a PDF or integrated into a report!






