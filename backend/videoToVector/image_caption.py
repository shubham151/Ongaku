import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')

def image_caption_genrator(image):
    API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
    headers = {"Authorization": os.getenv('BLIP_API_KEY') }
    
    response = requests.post(API_URL, headers=headers, data=image)

    return response.json()
