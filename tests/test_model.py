import numpy as np
from src.model import create_model

def test_model_prediction_range():
    model = create_model()
    # Dummy input
    dummy_img = np.random.rand(1, 224, 224, 3).astype(np.float32)
    prediction = model.predict(dummy_img)
    
    # Check that sigmoid output is between 0 and 1
    assert 0.0 <= prediction[0][0] <= 1.0