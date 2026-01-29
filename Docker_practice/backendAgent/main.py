# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent_main import run_agent
from core import core_status
import traceback
import os

app = FastAPI(title="Cognitic Agentic AI API")

# ==============================
# CORS CONFIG (LOCAL + PROD)
# ==============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://q-4-all-assignments-backend-and-so-iota.vercel.app",
        # "http://localhost:3001",
        # "https://*.vercel.app",     # Vercel frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# SCHEMAS
# ==============================
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str


# ==============================
# ROUTES
# ==============================
@app.get("/")
def home():
    return {"status": "Agent API is running 🚀"}

@app.get("/status")
def status():
    return core_status()

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    try:
        reply = run_agent(req.message)
        return {"reply": reply}

    except Exception as e:
        print("🔥 Server Error:", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal Server Error")
