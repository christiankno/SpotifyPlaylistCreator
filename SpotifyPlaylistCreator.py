import request
import json

from config import *
import requests


class PlaylistCreator:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token

    def create_playlist(self, name, description, public):
        request_body = json.dumps({
            'name': name,
            'description': description,
            'public': public
        })

        query 'https://api.spotify.com/v1/users/{}/playlist'.format(self.user_id)
        response = request.post(
            query,
            data=request_body,
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(self.spotify_token)
            }
        )
        response_json = response.json()

        return response_json['id']

    def get_spotify_uri(self, name, author):
        query = 'https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20'.format(name, author)
        response = requests.get(
            query,
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(self.spotify_token)
            }
        )
        response_json = response.json()
        songs = response_json['tracks']['items']

        uri = songs[0]['uri']

        return uri

