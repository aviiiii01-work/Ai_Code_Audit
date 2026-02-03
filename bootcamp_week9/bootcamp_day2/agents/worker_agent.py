from autogen_agentchat.agents import AssistantAgent
from config import model_client

worker_agent = AssistantAgent(
    name="worker",
    model_client=model_client,
    system_message="""ROLE: Worker Agent.
    TASK: Execute the steps provided by the Planner.
    STRICT RULES: Focus only on execution. Once complete, hand off to 'reflection'."""
)