import mlflow
import mlflow.keras
from data_loader import get_data_generators
from src.model import create_model

mlflow.set_experiment("Cats-vs-Dogs-Baseline")

with mlflow.start_run():
    # 1. Log parameters
    mlflow.log_param("image_size", 224)
    mlflow.log_param("batch_size", 32)
    
    train_gen, val_gen = get_data_generators('./data/raw/PetImages')
    model = create_model()
    
    # 2. Train
    history = model.fit(train_gen, validation_data=val_gen, epochs=10)
    
    # 3. Log metrics
    mlflow.log_metric("final_accuracy", history.history['accuracy'][-1])
    
    # 4. Save model
    mlflow.keras.log_model(model, "cnn_model")