from autogen_agentchat.agents import AssistantAgent
from config import model_client

answer_agent = AssistantAgent(
    name="answer_agent",
    model_client=model_client,
    system_message="""ROLE: Answer Agent.
    TASK: Provide a professional final response based on the summary.
    STRICT RULES: Start with 'Based on our research findings...'. Be helpful and polite."""
)