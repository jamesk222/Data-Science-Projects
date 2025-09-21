# Dockerfile
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py ./      
COPY data/models/best_pipeline.joblib ./models/
COPY data/models/metadata.json ./models/

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI app with Gunicorn + Uvicorn workers
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
