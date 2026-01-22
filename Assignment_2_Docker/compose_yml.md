# Docker Compose — Next.js & FastAPI Setup 🚀

This README contains **all commands** to run your Next.js and FastAPI Docker projects using a single **docker-compose.yml** file.

---

## 1️⃣ Create/Check `docker-compose.yml` in Root

```yaml
services:
  nextjs:
    image: <DOCKER_USERNAME>/nextjs-docker:latest
    container_name: nextjs-container
    ports:
      - "3000:3000"
    restart: unless-stopped

  fastapi:
    image: <DOCKER_USERNAME>/fastapi-docker:latest
    container_name: fastapi-container
    ports:
      - "8000:8000"
    restart: unless-stopped

- Replace <DOCKER_USERNAME> with your Docker Hub username

2️⃣ Login to Docker Hub
docker login
# Enter your Docker Hub username & password

3️⃣ Pull Images from Docker Hub
docker pull <DOCKER_USERNAME>/nextjs-docker:latest
docker pull <DOCKER_USERNAME>/fastapi-docker:latest

4️⃣ Run Containers Using Docker Compose
docker-compose up -d


-d runs containers in the background.

Next.js will run on http://localhost:3000
.

FastAPI will run on http://localhost:8000
.

5️⃣ Stop & Remove Containers
docker-compose stop
docker-compose down

6️⃣ Rebuild & Push Updated Images (Optional)
# Next.js
cd nextjs-docker
docker build -t <DOCKER_USERNAME>/nextjs-docker:latest .
docker push <DOCKER_USERNAME>/nextjs-docker:latest

# FastAPI
cd ../fastapi-docker
docker build -t <DOCKER_USERNAME>/fastapi-docker:latest .
docker push <DOCKER_USERNAME>/fastapi-docker:latest

# Relaunch updated containers
docker-compose up -d

7️⃣ Verify Running Containers
docker ps


Stops, removes, rebuilds, and pulls are all handled via the above commands.