# Billboard Top 100 Playlist Creator

## Description

This Python application scrapes the Billboard Top 100 songs for a given date and creates a playlist on Spotify using the `spotipy` library. The app fetches the list of songs from the Billboard website and then adds them to a new private Spotify playlist.

## Images

### 1. Playlist Created on Spotify
![Playlist Created on Spotify](https://github.com/user-attachments/assets/2d37dbab-1d80-4f75-9275-df3e961942f7)
This screenshot shows the private playlist created on Spotify, titled with the date of the Billboard Top 100 songs.

### 2. List of Song URIs in Python
![List of Song URIs in Python](https://github.com/user-attachments/assets/313a28c0-245a-4a0c-9767-5fdfda31e970)
Here, we see the output from the Python script where all the song URIs are printed in the console after they have been searched and fetched from Spotify.

### 3. Spotify Developer Dashboard
![Spotify Developer Dashboard](https://github.com/user-attachments/assets/21450c89-7a79-4dc0-83b8-07a1109bbe72)
This screenshot displays the Spotify Developer Dashboard where the app is registered, and the `Client ID`, `Client Secret`, and `Redirect URI` are set up to interact with the Spotify API.

## How to Create the Project

### Step 1: Set Up Spotify Developer App
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Log in to your Spotify account.
3. Create a new app to get your `Client ID` and `Client Secret`.
4. Set the **Redirect URI** (for example: `http://localhost:8888/callback`).

### Step 2: Install Required Libraries
Run the following command to install the required Python libraries:

```bash
pip install spotipy requests beautifulsoup4
```

# Billboard Top 100 Playlist Generator

This project allows you to generate a Spotify playlist containing the top 100 songs from Billboard for a specific date. The script scrapes the Billboard Top 100 page, fetches the song names, and creates a playlist on your Spotify account with those songs.

## Step 3: Write the Code

### 1. Import the Necessary Libraries:
- `requests`: for making HTTP requests.
- `BeautifulSoup`: for scraping the Billboard website.
- `spotipy`: for interacting with the Spotify API.

### 2. Scrape Billboard Top 100 Songs:
- Make a GET request to fetch the Billboard Top 100 page for a specific date.
- Parse the page using BeautifulSoup and extract the song names.

### 3. Authenticate with Spotify API:
- Use `SpotifyOAuth` to authenticate with the Spotify API using the credentials from your Spotify Developer Dashboard.
- Set the necessary scopes, such as `playlist-modify-private` and `playlist-modify-public`.

### 4. Create the Playlist and Add Songs:
- Use the `spotipy` library to create a playlist on the authenticated user's Spotify account.
- Fetch the song URIs from Spotify and add them to the newly created playlist.

## Step 4: Run the Script

Execute the Python script, and it will prompt you to log in to Spotify and authorize the app. Once authorized, it will create a playlist with the Billboard Top 100 songs for the date you provided.

## Step 5: Enjoy Your Playlist

After the script completes, you will find your new playlist in your Spotify account with all the top hits from the specified date!

---

**Note:** You will need to set up a Spotify Developer account and create an app to get your credentials (client ID and client secret) for authentication.
from the specified date!

---

**Note:** You will need to set up a Spotify Developer account and create an app to get your credentials (client ID and client secret) for authentication.
