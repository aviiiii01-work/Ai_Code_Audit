import asyncio
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from agents.research_agent import research_agent
from agents.summarizer_agent import summarizer_agent
from agents.answer_agent import answer_agent

async def main():
    user_task = input("Enter the task for the Agent System: ")
    token = CancellationToken()

    print(f"\n[SYSTEM]: Starting task: {user_task}")

    res_response = await research_agent.on_messages(
        [TextMessage(content=user_task, source="user")], 
        token
    )
    research_content = res_response.chat_message.content
    print(f"\n--- RESEARCH AGENT OUTPUT ---\n{research_content}")

    sum_response = await summarizer_agent.on_messages(
        [TextMessage(content=f"Summarize this with respect to query, content: {research_content}. Query: {user_task}", source="research_agent")], 
        token
    )
    summary_content = sum_response.chat_message.content
    print(f"\n--- SUMMARIZER OUTPUT ---\n{summary_content}")

    ans_response = await answer_agent.on_messages(
        [TextMessage(content=f"Provide the final answer for: {summary_content} based on the user query : {user_task}", source="summarizer_agent")], 
        token
    )
    print(f"\n--- FINAL ANSWER AGENT ---\n{ans_response.chat_message.content}")

if __name__ == "__main__":
    asyncio.run(main())