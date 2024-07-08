import base64
import requests
from dotenv import load_dotenv
import os
import json

# Load environment variables from a .env file
load_dotenv('../.env')

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_KEY')

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

# Get access token
access_token = get_access_token(client_id, client_secret)

def get_tracks_info(track_ids):
    url = "https://api.spotify.com/v1/tracks"
    params = {
        "ids": ",".join(track_ids)
    }

    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        params=params
    )

    if response.status_code == 200:
        return response.json()["tracks"]
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

# # Replace these with your actual Client ID and Client Secret

# # List of track IDs (replace with your actual track IDs)
# track_ids = [
#     '3n3Ppam7vgaVa1iaRUc9Lp',
#     '0eGsygTp906u18L0Oimnem',
#     '1dGr1c8CrMLDpV6mPbImSI',
#     # Add more track IDs as needed
# ]

# # Get track information
# tracks_info = get_tracks_info(access_token, track_ids)

# # Print track details
# for track in tracks_info:
#     print(f"ID: {track['id']}")
#     print(f"Name: {track['name']}")
#     print(f"Artists: {', '.join(artist['name'] for artist in track['artists'])}")
#     print(f"Album: {track['album']['name']}")
#     print(f"Release Date: {track['album']['release_date']}")
#     print(f"Popularity: {track['popularity']}")
#     print('-----------------------------')

# # Save the track details to a JSON file
# with open('track_details.json', 'w') as f:
#     json.dump(tracks_info, f, indent=4)

# print("Track details saved to 'track_details.json'.")

