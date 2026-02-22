import requests
import sys

def run_smoke_test():
    base_url = "http://localhost:30001"
    
    # 1. Check Health
    print("Testing /health...")
    health = requests.get(f"{base_url}/health")
    if health.status_code != 200:
        print("Health check failed!")
        sys.exit(1)

    # 2. Check Prediction
    print("Testing /predict...")
    # Using a dummy local image file
    with open("tests/resource/test_image.jpeg", "rb") as f:
        response = requests.post(f"{base_url}/predict", files={"file": f})
    
    if response.status_code != 200:
        print(f"Prediction failed with status {response.status_code}")
        sys.exit(1)
        
    print("Smoke test passed successfully!")

if __name__ == "__main__":
    run_smoke_test()