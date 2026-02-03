import asyncio
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo

model_client = OpenAIChatCompletionClient(
    model="mistral",
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    model_info=ModelInfo(
        vision=False,
        function_calling=True,
        json_output=True,
        family="mistral",
        structured_output=False,
        multiple_system_messages=False  
    )
)