from pcone.query import pinecone_query
from videoToVector.vectorizer import vector_query
from spotify.spotify_by_id import get_tracks_info

file_path = '..\\dataset\\sample1.mp4'

query = vector_query(file_path)

results = pinecone_query(query)

matches = [match.id for match in results.matches]

raw_response = get_tracks_info(matches)

for res in raw_response:
    print(res['album']['artists'][0]['name'])
    print(res['album']['images'][0]['url'])
    print("https://open.spotify.com/track/" + res['href'].split("/")[-1])
    print(res['name'])
    print(res['type'])
    print("===================")