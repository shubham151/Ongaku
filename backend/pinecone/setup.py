from dotenv import load_dotenv
import os
import pandas as pd
from pinecone import Pinecone, ServerlessSpec

load_dotenv('../.env')

# Initialize Pinecone with your API key
pc = Pinecone(api_key=os.getenv('PINE_KEY'))

# Define index name
index_name = 'musiceq'

# Check if index exists, create if not
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=9,  # Specify the dimension of your vectors
        metric="cosine",
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

# Read data from CSV, skipping the header row
csv_file_path = './tiktok_dataset.csv'
df = pd.read_csv(csv_file_path, skiprows=1)  # Skip the first row (header)

# Function to generate data in Pinecone format
def generate_data(df):
    data = []
    for idx, row in df.iterrows():
        _id = f"id_{idx}"
        vector_values = [float(val) for val in row.tolist()]  # Convert each value to float
        vector = {
            'id': _id,
            'values': vector_values
        }
        data.append(vector)
    return data

# Generate data in Pinecone format
data = generate_data(df)

# Connect to the index
index = pc.Index(index_name)

# Upload data to the index
index.upsert(vectors=data)

print(f"Successfully uploaded data to Pinecone index: {index_name}")

