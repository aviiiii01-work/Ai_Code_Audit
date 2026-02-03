import asyncio
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console
from orchestrator.planner import planner_agent
from agents.worker_agent import worker_agent
from agents.reflection import reflection_agent
from agents.validator import validator_agent
from config import model_client

async def main():
    termination = TextMentionTermination("FINAL ANSWER")

    team = SelectorGroupChat(
        participants=[planner_agent, worker_agent, reflection_agent, validator_agent],
        model_client=model_client,
        termination_condition=termination,
    )

    task = input("Enter your complex task: ")
    
    await Console(team.run_stream(task=task))

if __name__ == "__main__":
    asyncio.run(main())