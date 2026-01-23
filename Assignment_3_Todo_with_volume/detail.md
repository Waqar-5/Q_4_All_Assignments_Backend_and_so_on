# Next.js Todo App with Docker & Volume

A full-stack **Next.js Todo App** that persists data using **Docker volumes**. This project demonstrates building a Next.js application, containerizing it with Docker, using volumes for data persistence, and deploying a private image to Docker Hub.

---

## Table of Contents

* [Project Setup](#project-setup)
* [Run Locally](#run-locally)
* [Dockerize the App](#dockerize-the-app)
* [Docker Compose](#docker-compose)
* [Persistent Volume](#persistent-volume)
* [Push to Docker Hub](#push-to-docker-hub)
* [Pull & Run from Docker Hub](#pull--run-from-docker-hub)
* [Update Code and Rebuild](#update-code-and-rebuild)
* [Commands Summary](#commands-summary)

---

## Project Setup

1. Create a Next.js project:

```bash
npx create-next-app@latest todoapp
cd todoapp
```

2. Create a `todos.json` file (optional if using auto-create in app):

```bash
touch todos.json
```

3. Update `app/page.jsx` with your Todo app code (CRUD) in TypeScript/JS.

4. Install TypeScript types if needed:

```bash
npm install typescript @types/react @types/node
```

---

## Run Locally

```bash
npm install
npm run dev
```

Open: [http://localhost:3000](http://localhost:3000)

---

## Dockerize the App

1. Create `Dockerfile`:

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev"]
```

2. Build Docker image:

```bash
docker build -t my-nextjs-todo .
```

3. Run container:

```bash
docker run -d -p 3000:3000 --name todo-container my-nextjs-todo
```

---

## Docker Compose

1. Create `docker-compose.yml`:

```yaml
version: '3.8'
services:
  todoapp:
    build: .
    ports:
      - '3000:3000'
    volumes:
      - todo-data:/app/data
volumes:
  todo-data:
```

2. Start services:

```bash
docker-compose up -d
```

---

## Persistent Volume

1. Check Docker volumes:

```bash
docker volume ls
```

2. Inspect volume:

```bash
docker volume inspect todoapp_todo-data
```

3. Access volume contents:

```bash
docker run --rm -v todoapp_todo-data:/data alpine cat /data/todos.json
```

---

## Push to Docker Hub

1. Login to Docker Hub:

```bash
docker login
```

2. Tag the image:

```bash
docker tag my-nextjs-todo <username>/my-nextjs-todo:latest
```

3. Push to Docker Hub:

```bash
docker push <username>/my-nextjs-todo:latest
```

4. Make repository private via Docker Hub web UI (optional).

---

## Pull & Run from Docker Hub

1. Pull image on any machine:

```bash
docker pull <username>/my-nextjs-todo:latest
```

2. Run container with volume:

```bash
docker run -d -p 3000:3000 -v todo-data:/app/data --name todo-container <username>/my-nextjs-todo:latest
```

3. Check logs:

```bash
docker logs -f todo-container
```

Open: [http://localhost:3000](http://localhost:3000)

---

## Update Code and Rebuild

When you make changes to your app code:

1. Stop existing container:

```bash
docker stop todo-container
```

2. Remove container:

```bash
docker rm todo-container
```

3. Rebuild image:

```bash
docker build -t my-nextjs-todo .
```

4. Tag and push updated image:

```bash
docker tag my-nextjs-todo <username>/my-nextjs-todo:latest
docker push <username>/my-nextjs-todo:latest
```

5. Run updated container:

```bash
docker run -d -p 3000:3000 -v todo-data:/app/data --name todo-container <username>/my-nextjs-todo:latest
```

> ✅ Your volume `todo-data` ensures todos persist even after updating or removing containers.

---

## Commands Summary

```bash
# Project setup
npx create-next-app@latest todoapp
cd todoapp
touch todos.json
npm install
npm run dev

# Dockerize
Dockerfile -> build image
docker build -t my-nextjs-todo .

# Run container
 docker run -d -p 3000:3000 --name todo-container my-nextjs-todo

# Docker Compose
docker-compose up -d

# Volume check
docker volume ls
docker volume inspect todoapp_todo-data
docker run --rm -v todoapp_todo-data:/data alpine cat /data/todos.json

# Docker Hub push
docker login
docker tag my-nextjs-todo <username>/my-nextjs-todo:latest
docker push <username>/my-nextjs-todo:latest

# Pull and run from Docker Hub
docker pull <username>/my-nextjs-todo:latest
docker run -d -p 3000:3000 -v todo-data:/app/data --name todo-container <username>/my-nextjs-todo:latest

# Update code and rebuild
docker stop todo-container
docker rm todo-container
docker build -t my-nextjs-todo .
docker tag my-nextjs-todo <username>/my-nextjs-todo:latest
docker push <username>/my-nextjs-todo:latest
docker run -d -p 3000:3000 -v todo-data:/app/data --name todo-container <username>/my-nextjs-todo:latest
```

---

### ✅ Notes

* `todo-data` volume ensures todos persist even if container is removed.
* Use Docker Desktop UI to view running containers, volumes, and logs.
* Edit Next.js app anytime and rebuild image to update container.
* All commands are copy-paste ready for quick setup and deployment.
