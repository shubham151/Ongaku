import requests
from dotenv import load_dotenv
import os
load_dotenv('.env')

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": os.getenv('API_KEY') }

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("./extracted_frames/frame_00036.png")
print(output)
