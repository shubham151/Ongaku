from dotenv import load_dotenv
import os
from pinecone import Pinecone

load_dotenv('.env')

pc = Pinecone(api_key=os.getenv('PINE_KEY'))


def pinecone_query(vector):
    # Initialize Pinecone with your API key
    print("entry") 
    # Define index name
    index_name = 'musiceq'

    # Connect to the index
    index = pc.Index(index_name)

    results = index.query(
        vector=vector,
        top_k=5,
    )

    return results

