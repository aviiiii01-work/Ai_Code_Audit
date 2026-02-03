from autogen_agentchat.agents import AssistantAgent
from config import model_client

reflection_agent = AssistantAgent(
    name="reflection",
    model_client=model_client,
    system_message="""ROLE: Reflection Agent.
    TASK: Review the worker's output for depth and clarity.
    OUTPUT: Provide an improved version of the answer. Then hand off to 'validator'."""
)