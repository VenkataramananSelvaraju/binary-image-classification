import numpy as np
import pytest
from src.data_loader import get_data_generators # Assuming this is your function

def test_image_resizing():
    # Simulate a raw input (e.g., 500x500x3)
    # Ensure your preprocessing function converts it to 224x224x3
    pass

def test_pixel_normalization():
    # Ensure output pixels are in range [0, 1]
    # If the output contains values > 1, the test should fail
    pass