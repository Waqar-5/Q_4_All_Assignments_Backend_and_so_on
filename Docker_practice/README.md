# 🤖 Cognitic AI Chat

![Project Banner](/assets/pic1.png)
*Replace with your project banner or screenshot.*

Cognitic AI Chat is a modern, interactive AI assistant application with a **Next.js frontend** and a **FastAPI backend**, deployed seamlessly on Hugging Face Spaces. It allows users to chat with an AI agent in real-time, providing intelligent and contextual responses.

---

## 🌟 Live Demo

Check out the live project here: [Your Live Link](https://q-4-all-assignments-backend-and-so-iota.vercel.app/)

---

## 🏗️ Project Overview

* **Frontend:** Next.js 13 (React) with interactive chat UI, smooth animations, and random placeholder suggestions.
* **Backend:** FastAPI API serving an AI agent via `/chat` endpoint.
* **AI Agent:** Powered by your custom `agent_main.py` logic.
* **Deployment:** Hugging Face Spaces, Docker compatible, easy to extend.

---

## 📂 Project Structure

```
backend-agent/
│
├── main.py            # FastAPI app entrypoint
├── agent_main.py      # AI agent runner
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker configuration
├── frontend/          # Next.js app
│   ├── app/page.tsx   # Main frontend page
│   ├── chat.css       # Styling for chat
│   └── public/        # Static assets (avatars, icons)
└── README.md
```

---

## ⚡ Features

### Backend

* **FastAPI** for fast, asynchronous API.
* `/` endpoint: Check server status.
* `/chat` endpoint: Send messages to AI agent and receive responses.
* Easy integration with Hugging Face Spaces or any cloud deployment.
* Environment variable support for API keys and secrets.

### Frontend

* Interactive **chat interface** with smooth animations.
* Random **placeholder messages** to guide users.
* **Auto-scrolling chat window** for continuous conversation.
* Responsive **input and send button** with typing feedback.
* Distinct styling for **user vs AI messages** with avatar support.
* Fully editable and modular CSS for theme customization.

---

## 📦 Installation & Setup

### Backend

```bash
git clone https://huggingface.co/spaces/waqar5/backend-agent.git
cd backend-agent
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install --upgrade pip
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🛠️ API Usage

### Check server status

```
GET /
Response:
{
  "status": "Agent API is running 🚀"
}
```

### Send a chat message

```
POST /chat
Body:
{
  "message": "Hello, AI!"
}

Response:
{
  "reply": "Hi there! How can I assist you today?"
}
```

*Swagger docs available at `/docs` for testing endpoints.*

---

## 🎨 Frontend Usage

* Input your message in the chat box.
* Press **Enter** or click **Send**.
* AI response appears with typing animation.
* Scrollable chat interface with smooth transitions.

![Chat Screenshot](/assets/pic2.png)
*Replace with your frontend screenshot.*

---

## 🐳 Docker Deployment

Build and run Docker container:

```bash
docker build -t cognitic-ai-agent .
docker run -p 8000:8000 cognitic-ai-agent
```

---

## ⚙️ Environment Variables

* `API_KEY` – For AI services (if required)
* `MODEL_NAME` – Optional: specify custom AI model

---

<!-- ## 💡 Architecture Diagram

![Architecture](./path-to-architecture.png)
*Replace with a diagram showing Frontend ↔ Backend ↔ AI Agent.*

--- -->

## 🚀 Future Roadmap

* Add **multi-agent orchestration** support.
* Integrate **speech-to-text** and **text-to-speech**.
* Add **user authentication** for personal chat history.
* Optimize AI responses for speed and accuracy.
* Deploy **mobile-friendly version**.

---

## 👤 Author

**Waqar Ali**

* Email: [wa5134810@gmail.com](mailto:wa5134810@gmail.com)
* GitHub: [Waqar5](https://github.com/Waqar5)
* Hugging Face Spaces: [waqar5](https://huggingface.co/spaces/waqar5)

---

## 🔖 License

MIT License © 2026 Waqar Ali
