import os
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI, OpenAI

load_dotenv(find_dotenv())

# Use the standard flash model name
# CURRENT_MODEL = "gemini-2.0-flash" 
CURRENT_MODEL = "gemini-2.5-flash"


def get_async_client():
    return AsyncOpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

async def run_agent_stream(prompt: str):
    client = get_async_client()
    try:
        response = await client.chat.completions.create(
            model=CURRENT_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Respond immediately and concisely. Do not use a thinking phase."},
                {"role": "user", "content": prompt}
            ],
            stream=True
            # Removed reasoning_effort and extra_body to avoid 400 errors
        )
        async for chunk in response:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    except Exception as e:
        yield f"\n❌ Connection Error: {str(e)}"

def run_agent(prompt: str) -> str:
    sync_client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
    try:
        response = sync_client.chat.completions.create(
            model=CURRENT_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Respond immediately and concisely."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"