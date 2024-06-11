import os
import time
import requests
import base64
from tqdm import tqdm

# Define the endpoint URL
url = "http://localhost:8080/api/files/upload"

# Function to convert image to base64 string
def image_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_string

# Function to send POST request with payload
def send_post_request(file_name, base64_string):
    payload = {
        "fileName": file_name,
        "fileContent": base64_string
    }
    response = requests.post(url, json=payload)
    return response.text

# Path to the folder containing JPEG files
folder_path = "C:\\Users\\zaina\\htmlMocks\\images"

# Iterate over JPEG files in the folder
files = [file for file in os.listdir(folder_path) if file.endswith(".jpg")]
with tqdm(total=len(files), desc="Uploading files") as pbar:
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        base64_string = image_to_base64(file_path)
        response = send_post_request(file_name, base64_string)
        pbar.update(1)
        # time.sleep()  # Add a 2-second delay after each request

print("Upload complete")
