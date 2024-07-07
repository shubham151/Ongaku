import base64
import requests
from dotenv import load_dotenv
import os
import json

load_dotenv('.env')



client_id =os.getenv('CLIENT_ID') 
client_secret = os.getenv('CLIENT_KEY')



import base64
import requests
import json

# Function to get access token
def get_access_token(client_id, client_secret):
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={"Authorization": f"Basic {auth_header}"},
        data={"grant_type": "client_credentials"}
    )
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception(f"Failed to get access token: {response.status_code}, {response.text}")

access_token = get_access_token(client_id, client_secret)

# Function to get playlist items
def get_playlist_items(access_token, playlist_id):
    tracks = []
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {"Authorization": f"Bearer {access_token}"}

    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to get playlist items: {response.status_code}, {response.text}")

        data = response.json()
        tracks.extend(data["items"])

        url = data["next"]  # Get the next page URL, if any

    return tracks

# Function to get audio features
def get_audio_features(access_token, track_ids):
    track_features = []
    base_url = "https://api.spotify.com/v1/audio-features"
    for i in range(0, len(track_ids), 100):
        batch = track_ids[i:i + 100]
        ids = ",".join(batch)
        response = requests.get(
            f"{base_url}?ids={ids}",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        if response.status_code == 200:
            track_features.extend(response.json()["audio_features"])
        else:
            print(f"Error: {response.status_code}, {response.text}")
    return track_features


# Spotify's playlist ID
playlist_id = "37i9dQZF1DX0kbJZpiYdZl"

playlist_items = get_playlist_items(access_token, playlist_id)
track_ids = [item["track"]["id"] for item in playlist_items if item["track"]["id"]]

track_features = get_audio_features(access_token, track_ids)

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)

# Save the audio features to a JSON file
save_to_json(track_features, 'top_200_songs_features.json')
print("Audio features saved to top_200_songs_features.json")

# Print the audio features of the first track as an example
if track_features:
    print(json.dumps(track_features[0], indent=2))

