import os
from dotenv import load_dotenv
from openai import OpenAI, AsyncOpenAI

# Load environment variables from .env
load_dotenv()

# ============================
# Configuration for OpenRouter
# ============================
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# OpenRouter usually requires the provider prefix (e.g., openai/gpt-3.5-turbo)
MODEL_NAME = "openai/gpt-3.5-turbo"
# Headers required by OpenRouter for ranking and integration
HEADERS = {
    "HTTP-Referer": "http://localhost:8000", # Required for OpenRouter
    "X-Title": "Cognitic Agentic AI",        # Optional but recommended
}

# ============================
# Async client (streaming)
# ============================
def get_async_client():
    """
    Returns an AsyncOpenAI client configured for OpenRouter.
    """
    return AsyncOpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        default_headers=HEADERS
    )

async def run_agent_stream(prompt: str):
    """
    Streams chat responses from the OpenRouter API asynchronously.
    """
    client = get_async_client()
    try:
        response = await client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Respond immediately and concisely."
                },
                {"role": "user", "content": prompt}
            ],
            stream=True
        )
        async for chunk in response:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    except Exception as e:
        yield f"\n❌ Connection Error: {str(e)}"

# ============================
# Sync client (normal chat)
# ============================
def run_agent(prompt: str) -> str:
    client = OpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        default_headers={
            "HTTP-Referer": "http://localhost:8000", # Required
            "X-Title": "Cognitic AI",                 # Recommended
        }
    )
    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"