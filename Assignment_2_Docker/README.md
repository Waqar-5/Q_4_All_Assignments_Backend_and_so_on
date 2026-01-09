# Class 13 Docker Assignment 🚀

This repository contains **two simple containerized projects**:

1. **Next.js Docker App** – Front-end web app showing "Hello from Docker!"  
2. **FastAPI Docker App** – Backend API showing "Hello from FastAPI Docker!"  

Both projects are fully containerized using Docker and can be run locally with just a few commands.

---

## 📁 Repository Structure



class13-docker-assignment/
│
├── nextjs-docker/
│ ├── app/ # Next.js pages (App Router)
│ ├── Dockerfile # Docker configuration
│ ├── package.json # Node.js dependencies
│ └── package-lock.json # Node.js lock file
│
├── fastapi-docker/
│ ├── main.py # FastAPI app
│ ├── Dockerfile # Docker configuration
│ └── requirements.txt # Python dependencies
│
├── screenshots/
│ ├── nextjs-docker.png
│ ├── nextjs-docker-image.png
│ ├── fastapi-docker.png
│ └── fastapi-docker-image.png
│
└── README.md # This file



---


---

## 🟢 Next.js Docker Project

A simple **Next.js application** running inside a Docker container.

### 📸 Screenshot
![Next.js Docker Container](screenshots/nextjs-docker.png)

### 🛠️ How to Run Next.js App

1️⃣ Navigate to the project folder:

```bash
cd nextjs-docker

2️⃣ Build Docker Image:
docker build -t nextjs-docker .


3️⃣ Run Docker Container:
docker run -d -p 3000:3000 --name nextjs-container nextjs-docker


4️⃣ Open the App in your browser:
http://localhost:3000

You should see:
Hello from Docker!

5️⃣ Stop & Remove Container (Optional):
docker stop nextjs-container
docker rm nextjs-container


🟢 FastAPI Docker Project

A simple FastAPI backend API running inside a Docker container.

📸 Screenshot

🛠️ How to Run FastAPI App

1️⃣ Navigate to the project folder:
cd fastapi-docker


2️⃣ Build Docker Image:
docker build -t fastapi-docker .



3️⃣ Run Docker Container:
docker run -d -p 8000:8000 --name fastapi-container fastapi-docker


4️⃣ Access the App:

API endpoint: http://localhost:8000

Swagger docs: http://localhost:8000/docs

You should see:
{"message": "Hello from FastAPI Docker!"}

5️⃣ Stop & Remove Container (Optional):
docker stop fastapi-container
docker rm fastapi-container

📝 Notes

Any changes to source code require rebuilding the Docker image:

docker build -t <image-name> .


Use localhost instead of 0.0.0.0 in your browser.

Both projects can run on Windows, Mac, and Linux with Docker Desktop.

Make sure ports 3000 (Next.js) and 8000 (FastAPI) are free.

🔹 References

Next.js Documentation

FastAPI Documentation

Docker Documentation