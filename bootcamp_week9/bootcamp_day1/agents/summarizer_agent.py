from autogen_agentchat.agents import AssistantAgent
from config import model_client

summarizer_agent = AssistantAgent(
    name="summarizer_agent",
    model_client=model_client,
    system_message="""ROLE: Information Summarizer.
    TASK: Extract 3 key bullet points from the research provided.
    STRICT RULES: Do not add external info. Do not answer the user. Focus only on distillation."""
)