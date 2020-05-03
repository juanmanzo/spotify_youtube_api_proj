# Youtube/Spotify API Project
Creates Spotify playlists using your Youtube Playlists
## Installation
Install Google APIs Client Library for Python:
```bash
pip install --upgrade google-api-python-client
```
Install google-auth-oauthlib and google-auth-httplib2 libraries for user authorization:
```bash
pip install --upgrade google-auth-oauthlib google-auth-httplib2
```
Install [Spotipy Library](https://github.com/plamere/spotipy):
```bash
pip install spotipy --upgrade
```

## Usage
### Youtube API
1.Create a Google api key

2.Create an OAuth 2.0 client ID

3.Download the JSON file that contains your OAuth 2.0 credentials.

proj_keys.yt_api_key = 'Your youtube/google api key'

proj_keys.yt_client_secret_file = 'Your JSON file'
### Spotify API
1. Create a [Spotify Client ID](https://developer.spotify.com/dashboard/login)

2. Get Client Secret

proj.client_id='Your Client ID'

proj.client_secret='Your Client Secret'

### Create Spotify Playlist using Youtube Playlist
Create a SpotifyMaker Object

Call the makeYoutubePlaylist() method 

