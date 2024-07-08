import os
import base64
from flask import Flask, jsonify, request
from pcone.query import pinecone_query
from videoToVector.vectorizer import vector_query
from spotify.spotify_by_id import get_tracks_info

app = Flask(__name__)

@app.route('/', methods=['POST'])
def vector_generator():
    data = request.json
    print(data)
    encoded_video = data.get('video')
    decoded_video = base64.base64decode(encoded_video)

    file_path = '.\\data\\video.mp4'

    with open(file_path, 'wb') as video_file:
        video_file.write(decoded_video)
    
    query = vector_query(file_path)
    
    results = pinecone_query(query)

    matches = [match.id for match in results.matches]

    raw_response = get_tracks_info(matches)

    response = []

    for res in raw_response:
        track = {}
        track["Artist"] = res['album']['artists'][0]['name']
        track["Thumbnail"] = res['album']['images'][0]['url']
        track["URL"] = res['href']
        track["Name"] = res['name']
        response.append(track)

    return jsonify(response)

    # if os.path.exists(file_path):
    #     os.remove(file_path)

if __name__ == '__main__':
    app.run(debug=True)
