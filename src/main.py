from fastapi import FastAPI, UploadFile, File
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import os

MODEL_PATH = "models/model_v1.h5"

app = FastAPI()

# Load model globally to ensure it's initialized only once
# Load real model only if it exists, otherwise create a mock/placeholder
if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
else:
    print("Warning: Real model not found, using dummy structure for testing.")
    from src.model import create_model
    model = create_model()

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
    
    return {"label": label, "confidence": float(prediction[0][0])}