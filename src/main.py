from fastapi import FastAPI, UploadFile, File
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import io

app = FastAPI()

# Load the model at startup
MODEL_PATH = "models/model_v1.h5"
model = load_model(MODEL_PATH)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # 1. Read and preprocess image
    image = Image.open(io.BytesIO(await file.read())).convert('RGB')
    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0) # Shape: (1, 224, 224, 3)
    
    # 2. Inference
    prediction = model.predict(img_array)
    label = "Dog" if prediction[0][0] > 0.5 else "Cat"
    
    return {"label": label, "confidence": float(prediction[0][0])}