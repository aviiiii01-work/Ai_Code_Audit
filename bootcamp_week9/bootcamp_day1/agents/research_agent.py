from autogen_agentchat.agents import AssistantAgent
from config import model_client

research_agent = AssistantAgent(
    name="research_agent",
    model_client=model_client,
    system_message="""ROLE: Expert Researcher.
    TASK: Provide a technical deep-dive on the topic. 
    STRICT RULES: Raw data only. No summaries. No conversational fluff.
    MEMORY: Focused on the last 10 interactions."""
)