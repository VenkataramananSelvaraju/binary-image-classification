FROM python:3.12-slim

# Install system dependencies (required for image processing)
RUN apt-get update && apt-get install -y libgl1 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy necessary project folders
COPY src/ ./src/
COPY models/ ./models/

# Expose the API port
EXPOSE 8000

# Start the service
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]