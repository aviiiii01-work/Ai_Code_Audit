from autogen_agentchat.agents import AssistantAgent
from config import model_client

planner_agent = AssistantAgent(
    name="planner",
    model_client=model_client,
    system_message="""ROLE: Orchestrator / Planner.
    TASK: Break down the User Query into 3 distinct logical steps.
    OUTPUT: A numbered list of steps. 
    RULE: Do not solve the task. Only plan it. Then delegate to 'worker'."""
)