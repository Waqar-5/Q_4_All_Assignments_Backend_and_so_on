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
* [Commands Summary](#commands-summary)

---

## Project Setup

1. Create a Next.js project:

```bash
npx create-next-app@latest todoapp
cd todoapp
```

2. Create a `todos.json` file (optional if using app auto-create):

```bash
touch todos.json
```

3. Update `app/page.jsx` with your Todo app code (CRUD) in TypeScript/JS.

4. Install any necessary packages (if using TypeScript):

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

1. Create `Dockerfile` in project root:

```dockerfile
# Use Node image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the app
COPY . .

# Expose port
EXPOSE 3000

# Start the app
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

3. Access volume contents (optional):

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

3. Check logs and access app:

```bash
docker logs -f todo-container
```

Open: [http://localhost:3000](http://localhost:3000)

---

## Commands Summary

```bash
# Create project
npx create-next-app@latest todoapp
cd todoapp

# Run locally
npm install
npm run dev

# Build Docker image
docker build -t my-nextjs-todo .

# Run container
docker run -d -p 3000:3000 --name todo-container my-nextjs-todo

# Docker Compose
docker-compose up -d

# Check volumes
docker volume ls
docker volume inspect todoapp_todo-data

# Push to Docker Hub
docker login
docker tag my-nextjs-todo <username>/my-nextjs-todo:latest
docker push <username>/my-nextjs-todo:latest

# Pull & run from Docker Hub
docker pull <username>/my-nextjs-todo:latest
docker run -d -p 3000:3000 -v todo-data:/app/data --name todo-container <username>/my-nextjs-todo:latest
```

---

### ✅ Notes

* `todo-data` volume ensures `todos.json` persists even if container is removed.
* Use Docker Desktop UI to view running containers, volumes, and logs.
* You can edit the Next.js app at any time and rebuild the image to update the container.
