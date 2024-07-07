from dotenv import load_dotenv
import os
from pinecone import Pinecone

load_dotenv('../.env')

# Initialize Pinecone with your API key
pc = Pinecone(api_key=os.getenv('PINE_KEY'))

# Define index name
index_name = 'musiceq'

# Connect to the index
index = pc.Index(index_name)

test = index.query(
    vector=[0.49,0.15,0.13,0.7,0.28,0.51,0.8,0.27,0.52],
    top_k=3,
)

print(test)



