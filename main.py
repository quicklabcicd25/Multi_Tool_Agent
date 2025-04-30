import os
from dotenv import load_dotenv
from workflows.research_flow import build_research_workflow

load_dotenv()

if __name__ == "__main__":
    graph = build_research_workflow()
    query = input(" what are the AI trends in education?")
    result = graph.invoke(query)
    
    print("\n✅ Final Answer:\n")
    print(result)