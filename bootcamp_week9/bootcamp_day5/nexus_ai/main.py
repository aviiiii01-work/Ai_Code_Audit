import asyncio
import os
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console
from autogen_agentchat.conditions import TextMentionTermination 
from config import AGENT_SPECS

async def run_nexus():
    agents = []
    for name, spec in AGENT_SPECS.items():
        agent = AssistantAgent(
            name=name,
            model_client=spec["client"],
            system_message=spec["msg"]
        )
        agents.append(agent)

    
    termination = TextMentionTermination("TERMINATE")

    nexus_team = SelectorGroupChat(
        participants=agents, 
        model_client=AGENT_SPECS["Orchestrator"]["client"],
        termination_condition=termination,
        max_turns=12, 
        selector_prompt="""You are the Orchestrator. 
        Enforce this sequence: Planner -> Researcher -> Coder -> Critic -> Optimizer -> Validator -> Reporter.
        Do not allow agents to repeat previous points. 
        The Reporter must end the final summary with 'TERMINATE'.
        Roles available: {roles}"""
    )

    print("========================================")
    print("NEXUS AI: PRODUCTION MODE")
    print("========================================")

    while True:
        try:
            user_task = input("\n[User]: ").strip()
            if user_task.lower() in ["exit", "quit"]: break
            if not user_task: continue

            stream = nexus_team.run_stream(task=user_task)
            await Console(stream)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\n[System Error]: {e}")

if __name__ == "__main__":
    if not os.path.exists("./logs"): os.makedirs("./logs")
    asyncio.run(run_nexus())