import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo

load_dotenv()

'''
groq_model = OpenAIChatCompletionClient(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    model_info=ModelInfo(
    vision=False,
    function_calling=True, 
    json_output=True, 
    structured_output=True, 
    family="unknown"
)
)'''

groq_model = OpenAIChatCompletionClient(
    model="llama-3.1-8b-instant", 
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    model_info=ModelInfo(
        vision=False, 
        function_calling=True, 
        json_output=True, 
        structured_output=True,
        family="unknown"
    )
)


AGENT_SPECS = {
    "Orchestrator": {"client": groq_model, "msg": "You are the conductor. Keep responses short. Call the next agent."},
    "Planner": {"client": groq_model, "msg": "Provide a 3-step plan. Be concise. Max 100 words."},
    "Researcher": {"client": groq_model, "msg": "Add 2-3 technical details only. Be brief."},
    "Coder": {"client": groq_model, "msg": "Write a short Python snippet for the core logic."},
    "Analyst": {"client": groq_model, "msg": "Identify 1 key data risk. Be brief."},
    "Critic": {"client": groq_model, "msg": "CRITIQUE: Find one flaw in 20 words or less."},
    "Optimizer": {"client": groq_model, "msg": "Fix the flaw identified by Critic quickly."},
    "Validator": {"client": groq_model, "msg": "Verify requirements are met. Yes/No + 1 sentence."},
    "Reporter": {"client": groq_model, "msg": "Summarize everything in a short paragraph. End with: TERMINATE"}
}