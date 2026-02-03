from autogen_ext.models.ollama import OllamaChatCompletionClient

model_client = OllamaChatCompletionClient(
    model="mistral",
    host="http://localhost:11434",
)
