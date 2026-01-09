This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.





# Next.js Docker Project

A simple **Next.js application** containerized using **Docker**.  
This project displays a friendly message: **"Hello from Docker!"** and demonstrates how to run a Next.js app inside a Docker container.

---

## 📁 Project Structure

nextjs-docker/
│
├── app/ # Next.js pages (App Router)
│ └── page.tsx # Home page showing "Hello from Docker!"
├── Dockerfile # Docker configuration
├── package.json # Node.js dependencies
├── package-lock.json # Node.js lock file
└── .dockerignore # Files/folders ignored by Docker

yaml
Copy code

---

## 🐳 Prerequisites

- Docker installed on your system (Docker Desktop)
- Node.js (optional, only if you want to run outside Docker)
- Git (optional, if cloning from GitHub)

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/class13-docker-assignment.git
cd class13-docker-assignment/nextjs-docker
2. Build Docker Image
bash
Copy code
docker build -t nextjs-docker .
3. Run Docker Container
bash
Copy code
docker run -d -p 3000:3000 --name nextjs-container nextjs-docker
-d → Run container in detached mode

-p 3000:3000 → Map container port 3000 to localhost:3000

--name nextjs-container → Name of the container

4. Access the App
Open your browser and go to:

arduino
Copy code
http://localhost:3000
You should see:

css
Copy code
Hello from Docker!
This Next.js app is running inside a Docker container 🚀
🛠️ Stop & Remove Container
To stop and remove the container:

bash
Copy code
docker stop nextjs-container
docker rm nextjs-container
📸 Screenshots
Running Docker Container in Docker Desktop

Docker Image

✅ Features
Next.js application with App Router

Fully containerized using Docker

Easy to build and run with a single command

Friendly message to test Docker setup

💡 Notes
Make sure port 3000 is free on your local machine

Any changes to page.tsx require rebuilding the Docker image to reflect updates

Works on Windows, Linux, and Mac with Docker Desktop installed

📚 References
Next.js Documentation

Docker Documentation