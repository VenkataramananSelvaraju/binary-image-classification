FROM python:3.12-slim

# Install system dependencies for image processing
RUN apt-get update && apt-get install -y libgl1-mesa-glx

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and model
COPY src/ ./src/
COPY models/ ./models/

# Set environment variable to allow module imports
ENV PYTHONPATH=/app

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]