from fastapi import FastAPI
from pydantic import BaseModel
from agent_main import run_agent

app = FastAPI(title="Cognitic Agentic AI API")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Agent API is running 🚀"}

@app.post("/chat")
def chat(req: ChatRequest):
    reply = run_agent(req.message)
    return {"reply": reply}

