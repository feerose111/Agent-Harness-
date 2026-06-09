from deepagents import create_deep_agent
from database.dependency import get_llm

model = get_llm()

agent = create_deep_agent(
    model = model,
    
)