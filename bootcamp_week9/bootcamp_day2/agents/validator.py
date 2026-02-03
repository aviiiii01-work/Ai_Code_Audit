from autogen_agentchat.agents import AssistantAgent
from config import model_client

validator_agent = AssistantAgent(
    name="validator",
    model_client=model_client,
    system_message="""ROLE: Validator Agent.
    TASK: Check for errors, hallucinations, or missing requirements.
    FINAL STEP: If correct, end with 'FINAL ANSWER:' followed by the text. 
    If incorrect, send back to 'worker' for revision."""
)