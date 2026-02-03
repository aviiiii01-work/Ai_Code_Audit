import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelFamily

from tools.db_agent import run_postgresql_query
from tools.file_agent import read_or_write_file
from tools.code_executor import execute_python_logic

async def main():
    model_client = OpenAIChatCompletionClient(
        model="mistral",
        base_url="http://localhost:11434/v1",
        api_key="ollama",
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "family": ModelFamily.UNKNOWN,
        },
        extra_create_args={"parallel_tool_calls": False} 
    )

    boss_agent = AssistantAgent(
        name="autonomous_operator",
        model_client=model_client,
        tools=[run_postgresql_query, read_or_write_file, execute_python_logic],
        reflect_on_tool_use=True,
        system_message=(
            "You are a system operator that executes tasks using tools. "
            "STRICT RULES:\n"
            "1. To perform math/logic, call 'execute_python_logic'.\n"
            "2. To save ANY content to a file, you MUST call 'read_or_write_file' with mode='write'.\n"
            "3. Do not just describe how to save a file; actually CALL the tool.\n"
            "4. If a task has two parts (calculate AND save), you must call TWO tools in sequence.\n"
            "5. After the final tool call confirms success, say 'TERMINATE'."
        )
    )

    print("--- Autonomous Multi-Agent System ---")
    user_task = input("Enter your task: ")  

    print(f"\n Orchestrating tools for task...")
    await Console(boss_agent.run_stream(task=user_task))

if __name__ == "__main__":
    asyncio.run(main())