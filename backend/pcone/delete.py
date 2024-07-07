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



index.delete(delete_all=True)
