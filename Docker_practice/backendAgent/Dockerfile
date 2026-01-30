FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]


# # =========================
# # 1️⃣ Base Image
# # =========================
# FROM python:3.11-slim

# # =========================
# # 2️⃣ Set working directory
# # =========================
# WORKDIR /app

# # =========================
# # 3️⃣ Copy only requirements first (for caching)
# # =========================
# COPY requirements.txt .

# # =========================
# # 4️⃣ Install dependencies
# # =========================
# RUN pip install --no-cache-dir --upgrade pip \
#     && pip install --no-cache-dir -r requirements.txt

# # =========================
# # 5️⃣ Copy app code
# # =========================
# COPY . .

# # =========================
# # 6️⃣ Environment variables (optional)
# # =========================
# # Make sure to add your secret API keys via Docker secrets or environment variables
# # ENV GEMINI_API_KEY="your_api_key_here"

# # =========================
# # 7️⃣ Expose port
# # =========================
# EXPOSE 8000

# # =========================
# # 8️⃣ Run the FastAPI app using Uvicorn
# # =========================
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
