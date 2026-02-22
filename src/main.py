from fastapi import FastAPI, UploadFile, File, Request
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import time
import logging
import csv
from datetime import datetime

MODEL_PATH = "models/model_v1.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api_monitor")

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Load and preprocess
    image = Image.open(io.BytesIO(await file.read())).convert('RGB')
    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Inference
    prediction = model.predict(img_array)
    label = "Dog" if prediction[0][0] > 0.5 else "Cat"

    log_prediction(
        input_data=file.filename, 
        prediction=str(prediction),
        label=label
    )
    
    return {"label": label, "confidence": float(prediction[0][0])}

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    # Log metrics (Request count & Latency)
    logger.info(f"Path: {request.url.path} | Method: {request.method} | Latency: {process_time:.4f}s")
    return response

def log_prediction(input_data, prediction, label=None):
    with open("logs/predictions.csv", "a", newline='') as f:
        writer = csv.writer(f)
        # Record the input, result, and optional truth for performance analysis
        writer.writerow([datetime.now(), input_data, prediction, label])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)