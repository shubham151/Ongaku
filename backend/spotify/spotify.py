import base64
import requests
from dotenv import load_dotenv
import os

load_dotenv('../.env')

def get_access_token(client_id, client_secret):
    # Encode client ID and client secret
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    
    # Request for access token
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "Authorization": f"Basic {auth_header}"
        },
        data={
            "grant_type": "client_credentials"
        }
    )
    
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception(f"Failed to get access token: {response.status_code}, {response.text}")

# Replace these with your actual Client ID and Client Secret
def get_recommendations(access_token, target_danceability, target_energy, target_valence):
    parameters = {
        "limit": 10,  # Number of recommendations
        "market": "US",
        "seed_genres": "pop",  # Seed genre(s)
        "target_danceability": target_danceability,
        "target_energy": target_energy,
        "target_valence": target_valence  # Happiness
    }

    response = requests.get(
        "https://api.spotify.com/v1/recommendations",
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        params=parameters
    )

    i=0
    if response.status_code == 200:
        recommendations = response.json()
        for track in recommendations["tracks"]:
            if i == 0:
                print(track)
            i+=1
            print(f"Track: {track['name']} by {track['artists'][0]['name']}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Replace with your desired feature values
target_danceability = 0.8
target_energy = 0.7
target_valence = 0.9


client_id =os.getenv('CLIENT_ID') 
client_secret = os.getenv('CLIENT_KEY')

access_token = get_access_token(client_id, client_secret)
#print(f"Access Token: {access_token}")



get_recommendations(access_token, target_danceability, target_energy, target_valence)

