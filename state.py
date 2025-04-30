# state.py
from pydantic import BaseModel
from typing import Optional

class ResearchState(BaseModel):
    query: str
    research_results: Optional[str] = None
    response: Optional[str] = None