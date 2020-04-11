import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import proj_keys
scope = 'user-top-read user-library-read'
username = keys
SPOTIPY_CLIENT_ID = proj_keys.client_id
SPOTIPY_CLIENT_SECRET = proj_keys.client_secret
print(SPOTIPY_CLIENT_ID)


spcl = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))
'''
token = util.prompt_for_user_token(username, scope, client_id = SPOTIPY_CLIENT_ID, client_secret = SPOTIPY_CLIENT_SECRET, redirect_uri = 'http://localhost/')
if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
    sp.trace = False
    ranges = ['short_term', 'medium_term', 'long_term']
    for rang in ranges:
        print("range:", rang)
        results = sp.current_user_top_artists(time_range=rang, limit=50)
        for i, item in enumerate(results['items']):
            print(i, item['name'])
        print()
else:
    print("Can't get token for", username)
'''
track = 'Santeria'
artist = 'Sublime'
query = track + " " + artist
results = spcl.search(q=query, type='track')
results = results['tracks']['items']
for result in results:
    print(str(result['artists'][0]['name']) +": " + str(result['name']))
    print("\n \n")
