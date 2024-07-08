import base64
from flask import Flask
from videoToVector.vectorizer import vector_query

app = Flask(__name__)

from flask import Flask, request
# ...

@app.route('/', methods=['GET'])
def vector_generator():
    data = request.json
    encoded_video = data.get('video')
    print(data.get('age'))
    return data

