from autogen_ext.models.openai import OpenAIChatCompletionClient

model_client = OpenAIChatCompletionClient(
    model="mistral",
    base_url="http://localhost:11434/v1",
    api_key="ollama", 
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": False,
        "family": "mistral",
    }
)