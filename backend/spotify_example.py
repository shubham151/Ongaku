# from dotenv import load_dotenv
import os
import base64
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from requests import post
import json
# load_dotenv()

client_id = '05444b5c971b43368d9fb4355a160bc6'
client_secret = '8e5b30e04ee443bb817c27fb452ebf16'
redirect_uri = 'https://localhost:8008/'
username = "31tlzsaiex7fyz6naqzatorciug4"
mood = 1.0

# client_credentials_manager = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
# sp = spotipy.Spotify(client_credentials_manager= client_credentials_manager)
# scope="user-read-recently-played user-top-read playlist-modify-public"
# token = util.promp
def get_token():
    # auth_string = client_id + ':' + client_secret
    # auth_bytes = auth_string.encode("utf-8")
    # auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")
    url = 'https://accounts.spotify.com/api/token'
    request_body = {
        "grant_type": 'client_credentials',
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": 'user-library-read user-top-read playlist-modify-public user-follow-read'
    }
    r = post(url = url, data = request_body)
    resp = r.json()
    if r.status_code != 200:
        raise Exception(f"Failed to get token: {r.content}")

    token_from_json = resp['access_token']
    return token_from_json

def get_auth_header(token):
    return {"Authorization":"Bearer "+token}
def authenticate_spotify(token):
    print("*************************  connecting to spotify  ****************************************")
    sp = spotipy.Spotify(auth=token)
    print(sp)
token= get_token()
authenticate_spotify(token)
# retrieve_token()
print(token)

