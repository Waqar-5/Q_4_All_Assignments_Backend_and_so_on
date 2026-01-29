# agent_main.py
import os
from dotenv import load_dotenv, find_dotenv
from agents import Agent, Runner
from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI

load_dotenv(find_dotenv())

_agent = None

def get_agent():
    global _agent
    if _agent is None:
        client = AsyncOpenAI(
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )

        model = OpenAIChatCompletionsModel(
            model="gemini-2.5-flash",
            openai_client=client
        )

        _agent = Agent(
            name="Assistant",
            model=model
        )

    return _agent


async def run_agent_stream(prompt: str):
    agent = get_agent()
    try:
        result = Runner.run_streamed(
            starting_agent=agent,
            input=prompt
        )

        async for event in result.events():
            if event.type == "response.output_text.delta":
                yield event.delta

    except Exception as e:
        yield f"\n❌ Error: {e}"


def run_agent(prompt: str) -> str:
    agent = get_agent()
    try:
        result = Runner.run_sync(
            starting_agent=agent,
            input=prompt
        )
        return result.final_output
    except Exception as e:
        return f"❌ Error: {e}"
