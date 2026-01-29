from fastapi import FastAPI, HTTPException
from agent_main import run_agent
import uvicorn

app = FastAPI(title="Cognitic Agentic AI API")

@app.get("/")
def home():
    return {"status": "Agent API is running 🚀"}

@app.post("/chat")
def chat(message: str): # Simplified for testing
    reply = run_agent(message)
    return {"reply": reply}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)