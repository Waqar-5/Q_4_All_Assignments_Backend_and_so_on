# FastAPI Docker Project 🚀

A simple FastAPI application containerized using Docker.  
This project allows users to run a FastAPI server locally in a Docker container and access the API and interactive Swagger documentation.

---

## 🔹 Features

- FastAPI backend
- Dockerized for easy deployment
- Interactive API docs using Swagger UI
- Ready-to-run with a single Docker command

---

## 📁 Project Structure

fastapi-docker/
├── main.py # FastAPI application
├── Dockerfile # Dockerfile to build the image
└── README.md # This file


---

## 🐍 main.py Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI Docker!"}
🐳 Docker Instructions
1️⃣ Build Docker Image
From the fastapi-docker project folder:


docker build -t fastapi-docker .
This will create a Docker image named fastapi-docker.

2️⃣ Run Docker Container


docker run -p 8000:8000 fastapi-docker
-p 8000:8000 maps container port 8000 → your computer port 8000.

This allows you to open the app in your browser at localhost.

3️⃣ Access the App
Open your browser and go to:

API endpoint: http://localhost:8000

Swagger docs: http://localhost:8000/docs

You should see:

{"message": "Hello from FastAPI Docker!"}
4️⃣ Stop Running Container (Optional)
To stop the container:


docker ps          # List running containers
docker stop <id>   # Stop container by ID or name
docker rm <id>     # Remove container
🖼 Docker Desktop Screenshots
Include your Docker Desktop Images and Running Containers screenshots here.

⚠️ Notes for Users
Never click URLs with 0.0.0.0 — use localhost:8000 in your browser.

Logs may show 0.0.0.0:8000 — this is normal and only for internal container networking.

If you want to share the app publicly, host it using platforms like Railway, Render, or Fly.io.

📌 Quick Tips
Modify main.py to add more endpoints.

Always rebuild the Docker image if you make changes:


docker build -t fastapi-docker .
Then run the container again with -p 8000:8000.

