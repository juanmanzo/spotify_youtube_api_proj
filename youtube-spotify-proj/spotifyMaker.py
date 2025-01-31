import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import proj_keys
import ytapi
scope = 'user-top-read user-library-read playlist-modify-public playlist-modify-private'
username = proj_keys.usr
SPOTIPY_CLIENT_ID = proj_keys.client_id
SPOTIPY_CLIENT_SECRET = proj_keys.client_secret

class SpotifyMaker(object):
    def __init__(self):
        #Initialize 
        self.spcl = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))
        self.token = util.prompt_for_user_token(username, scope, client_id = SPOTIPY_CLIENT_ID, client_secret = SPOTIPY_CLIENT_SECRET, redirect_uri = 'http://localhost/')
        self.sp = spotipy.Spotify(auth=self.token)

    def getTrackInfo(self, track, artist):
        query = track + " " + artist
        results = self.spcl.search(q=query, type='track')
        if len(results['tracks']['items']) != 0:
            results = results['tracks']['items']
            for result in results:
                print(str(result['artists'][0]['name']) +": " + str(result['name']) + str(result['id']))
                print("\n \n")
        else:
            print("Cannot find track named: " + track + " by " + artist)

    def getSongForPlaylist(self, title):
        results = self.spcl.search(q=title, type='track')
        if len(results['tracks']['items']) != 0:
            results = results['tracks']['items'][0]
            songId = results['id']
            return songId
        else:
            print("Cannot find: " + title)
            return ""

    def makePlaylist(self, listofsongs):
        songIds = []
        if self.token:
            playlist = self.sp.user_playlist_create(username, "Youtube Playlist")
            playlistId = playlist['id']
            for song in listofsongs:
                songId = self.getSongForPlaylist(song)
                if len(songId) != 0:
                    songIds.append(songId)
            self.sp.user_playlist_add_tracks(username, playlistId, songIds)
        else:
            print("Can't get token for ", username)

    def makeYoutubePlaylist(self):
        yt = ytapi.YoutubeAPI()
        listofsongs = yt.transferPlaylistToSpotify()
        if len(listofsongs) != 0:
            songIds = []
            if self.token:
                sp = spotipy.Spotify(auth=self.token)
                playlist = self.sp.user_playlist_create(username, "Youtube Playlist")
                playlistId = playlist['id']
                for song in listofsongs:
                    songId = self.getSongForPlaylist(song)
                    if len(songId) != 0:
                        songIds.append(songId)
                self.sp.user_playlist_add_tracks(username, playlistId, songIds)
            else:
                print("Can't get token for ", username)



if __name__ == '__main__':
    sm = SpotifyMaker()
    sm.getTrackInfo('Santeria', 'Sublime')
    #sm.makeYoutubePlaylist()
