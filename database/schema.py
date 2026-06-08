from pydantic import BaseModel
from typing import Optional

class AgentHarnessData(BaseModel):
    name : str 
    path : str
    description : Optional[str] = None