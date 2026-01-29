---
title: Cognitic AI Backend
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
sdk_version: "0.0.1"
app_file: main.py
pinned: false
---




# Cognitic Agentic AI API

This is the backend API for the Cognitic Agentic AI project. It uses **FastAPI** to handle chat requests with an agent powered by OpenAI/Gemini models.

## Endpoints

- **GET /** – Health check, returns `{"status": "Agent API is running 🚀"}`
- **GET /status** – Returns core status
- **POST /chat** – Send a message, returns a reply

### How to run

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
