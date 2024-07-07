from dotenv import load_dotenv
import os
from pinecone import Pinecone

load_dotenv('../.env')
print(os.getenv('PINE_KEY'))
pc = Pinecone(api_key=os.getenv('PINE_KEY'))


def pinecone_query(vector):
    # Initialize Pinecone with your API key
    
    # Define index name
    index_name = 'musiceq'

    # Connect to the index
    index = pc.Index(index_name)

    results = index.query(
        vector=vector,
        top_k=5,
    )

    return results

pinecone_query([0.2,0.4,0.6,0.9,0.2,0.4,0.6,0.9,100])
