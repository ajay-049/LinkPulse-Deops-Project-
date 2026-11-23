# Use slim image to reduce size and security vulnerabilities
FROM python:3.11-slim

# Prevent Python from buffering stdout/stderr (so 'kubectl logs' works in real time)
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements first to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

# Security best practice: never run production containers as root
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
