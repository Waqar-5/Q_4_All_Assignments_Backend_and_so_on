# 🤖 Backend Agentic AI API

A **production-ready Agentic AI backend** built with **FastAPI**, containerized using **Docker**, and deployed on **Hugging Face Spaces**. This project demonstrates how to expose an AI agent as a clean REST API and connect it with modern LLM providers like **OpenRouter (free models)**.

---

## 🚀 Live Overview

* **Framework**: FastAPI
* **Deployment**: Hugging Face Spaces (Docker)
* **AI Provider**: OpenRouter (Free Models)
* **Server**: Uvicorn
* **Architecture**: Agent-based backend

This backend is designed to be:

* ✅ Simple
* ✅ Scalable
* ✅ Frontend-ready
* ✅ Cloud deployable

---

## 📂 Project Structure

```
backend-agent/
│
├── main.py              # FastAPI entry point
├── agent_main.py        # Core agent logic
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build instructions
├── .env                 # Environment variables (API keys)
└── README.md            # Project documentation
```

---

## 🧠 How the Agent Works

1. Client sends a message to `/chat`
2. FastAPI receives the request
3. Message is passed to `run_agent()`
4. Agent communicates with OpenRouter LLM
5. Response is returned as JSON

---

## 🧩 API Endpoints

### 🔹 Health Check

```http
GET /
```

**Response**

```json
{
  "status": "Agent API is running 🚀"
}
```

---

### 🔹 Chat with Agent

```http
POST /chat
```

**Request Body**

```json
{
  "message": "Hello Agent"
}
```

**Response**

```json
{
  "reply": "Hello! How can I help you today?"
}
```

---

## 🧪 Swagger UI (Built-in)

FastAPI automatically provides interactive docs:

```
/docs
```

You can test all endpoints directly from the browser.

---

## 🐳 Docker Setup

### Dockerfile (Key Idea)

* Uses lightweight Python base image
* Installs dependencies via `requirements.txt`
* Runs FastAPI using Uvicorn

### Build Locally

```bash
docker build -t backend-agent .
```

### Run Locally

```bash
docker run -p 8000:8000 backend-agent
```

---

## ☁️ Deployment on Hugging Face Spaces

1. Create a **Docker Space**
2. Push this repository to Hugging Face
3. Add secrets in **Space Settings**:

```env
OPENROUTER_API_KEY=your_api_key_here
```

4. Space auto-builds and deploys 🚀

---

## 🔐 Environment Variables

Create a `.env` file locally:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Never commit API keys to GitHub.

---

## 🧠 Why This Project Is Powerful

* 🧩 Agent-based architecture
* 🌐 Clean REST API
* 🐳 Dockerized deployment
* 🤗 Hugging Face compatible
* 🔁 Easy model switching (OpenRouter)
* ⚡ Fast & lightweight

---

## 🛠 Tech Stack

* **Python 3.11**
* **FastAPI**
* **Uvicorn**
* **Docker**
* **OpenRouter API**
* **Hugging Face Spaces**

---

## 📈 Future Enhancements

* ✅ Streaming responses
* ✅ Conversation memory
* ✅ Authentication
* ✅ Frontend (React / Next.js)
* ✅ Multi-agent orchestration

---

## 👤 Author

**Waqar Ali**
Agentic AI Developer | FastAPI | Docker | Hugging Face

---

## ⭐ Support

If you like this project:

* ⭐ Star the Space
* 🤝 Share with others
* 🧠 Build your own agent on top of it

---

### 🚀 Ready to build the future with Agentic AI

Happy coding! 🤖✨
