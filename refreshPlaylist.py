import spotipy
import config
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.client_id,
                                               client_secret=config.client_secret,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-top-read playlist-modify-public playlist-modify-private"))

playlist_id = config.playlist_id
newTracks = []

results = sp.current_user_top_tracks(limit=config.numOfSongs, offset=0, time_range='short_term')
for idx, item in enumerate(results['items']):
    newTracks.append(item['id'])

sp.playlist_replace_items(playlist_id, newTracks)