from pinecone.query import pinecone_query
from videoToVector.vectorizer import vector_query

file_path = '..\\dataset\\sample1.mp4'

query = vector_query(file_path)

results = pinecone_query(query)

print(results)