import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from pcone.query import pinecone_query
from videoToVector.vectorizer import vector_query
from spotify.spotify_by_id import get_tracks_info

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def vector_generator():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join('./data', 'video.mp4')
    file.save(file_path)

    try:
        query = vector_query(file_path)
        results = pinecone_query(query)
        matches = [match.id for match in results.matches]

        raw_response = get_tracks_info(matches)

        response = []
        for res in raw_response:
            track = {
                "artist": res['album']['artists'][0]['name'],
                "image": res['album']['images'][0]['url'],
                "songUrl": "https://open.spotify.com/track/" + res['href'].split("/")[-1],
                "songName": res['name']
            }
            response.append(track)

        return jsonify(response)

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == '__main__':
    app.run(debug=True)
