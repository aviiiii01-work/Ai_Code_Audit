import asyncio
import json
from autogen_agentchat.agents import AssistantAgent
from autogen_core.memory import MemoryContent, MemoryMimeType
from config import model_client
from memory.vector_store import FAISSVectorMemory
from memory.long_term_db import init_db, save_to_long_term_db, get_all_db_facts
from memory.session_memory import SessionMemory 

async def main():
    await init_db()
    vector_mem = FAISSVectorMemory()
    short_term = SessionMemory(max_messages=5) 
    
    agent = AssistantAgent(
        name="MemoryAgent",
        model_client=model_client,
        memory=[vector_mem],
        tools=[save_to_long_term_db, get_all_db_facts],
        system_message="You are a helpful assistant. Use tools to fetch data. If you see tool results, use them to answer the user."
    )

    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit': break
        
        await vector_mem.add(MemoryContent(content=user_input, mime_type=MemoryMimeType.TEXT))
        short_term.add_message("user", user_input)
        
        response = await agent.run(task=user_input)
        msg_text = response.messages[-1].content

        if "get_all_db_facts" in msg_text or "TOOL_CALLS" in msg_text:
            db_data = await get_all_db_facts()
            
            follow_up_task = f"I have fetched the data from the database for you. Here it is: {db_data}. Now, answer the user's question: '{user_input}'"
            final_response = await agent.run(task=follow_up_task)
            print(f"\nMemoryAgent: {final_response.messages[-1].content}\n")
        
        elif "save_to_long_term_db" in msg_text or "Register" in user_input:
            await save_to_long_term_db(user_input)
            print("\n>>> SYSTEM: Fact saved to SQLite.")
            print(f"\nMemoryAgent: {msg_text}\n")
            
        else:
            print(f"\nMemoryAgent: {msg_text}\n")

if __name__ == "__main__":
    asyncio.run(main())