import os
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

def download_and_extract():
    api = KaggleApi()
    api.authenticate()
    
    # Dataset identifier from the URL
    dataset = 'bhavikjikadara/dog-and-cat-classification-dataset'
    download_path = './data/raw'
    
    if not os.path.exists(download_path):
        os.makedirs(download_path)
        
    print("Downloading dataset...")
    api.dataset_download_files(dataset, path=download_path, unzip=True)
    print("Extraction complete.")

if __name__ == "__main__":
    download_and_extract()