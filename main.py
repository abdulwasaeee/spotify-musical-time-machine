import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="------",
    client_id="------",
    client_secret="------",
    show_dialog=True,
    cache_path="token.txt"
))

user_id = sp.current_user()["id"]


year = input("Which year would you like to travel to? Type this in the format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}", headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")
songs = [i.getText().strip() for i in soup.select("li ul li h3")]


song_uris = []
for song in songs:
    result = sp.search(song, limit=1, type="track")
    if result["tracks"]["items"]:
        song_uris.append(result["tracks"]["items"][0]["uri"])
        print(result["tracks"]["items"][0]["uri"])

playlist = sp.user_playlist_create(user=user_id, name=f"Billboard Top 100 from {year}", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(f"Playlist 'Billboard Top 100 from {year}' created and songs added!")
