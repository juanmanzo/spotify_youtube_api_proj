import os
import google_auth_oauthlib.flow
from apiclient.discovery import build
import proj_keys

class YoutubeAPI(object):
	def __init__(self):
		scopes = ["https://www.googleapis.com/auth/youtube"]
		os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
		#Initialize credentials for public youtube information
		api_key = proj_keys.yt_api_key
		self.pub_youtube = build('youtube', 'v3', developerKey = api_key)

		#Initialize credentials for retrieving user Yotube information
		client_secrets_file = proj_keys.yt_client_secret_file
		flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
		self.credentials = flow.run_console()
		self.youtube = build('youtube', 'v3', credentials=self.credentials)

	def getUserSubscriptions(self):
		request = self.youtube.subscriptions().list(
        part="snippet", mine = True, maxResults = 20
    	)

		res  = request.execute()
		items = res['items']
		for item in items:
			print(item['snippet']['title'])

	def getYoutuberSubcriptions(self, channelIdVal):
		req = self.pub_youtube.subscriptions().list(part = 'snippet', channelId = channelIdVal)
		res  = req.execute()
		items = res['items']
		for item in items:
			print(item['snippet']['title'])

	def getYoutubeVideos(self, query):
		req  = self.pub_youtube.search().list(q= query, part = 'snippet', type = 'video')
		res  = req.execute()
		items = res['items']
		for item in items:
			print(item['snippet']['title'])

	def getUserPlaylists(self):
		req  = self.youtube.playlists().list(part = 'snippet', mine = True)
		res =  req.execute()
		items = res['items']
		for item in items:
			print(item)
			print(str(item['snippet']['title']))

	def getUserPlaylistSongs(self, playlistIdVal):
		#Takes in a playlistID, returns list of song titles from playlist
		newsong_titles = []
		req  = self.youtube.playlistItems().list(part = 'snippet', playlistId = playlistIdVal, maxResults = 50)
		res =  req.execute()
		items = res['items']
		for item in items:
			itemTitle = item['snippet']['title']
			newsong_titles.append(self.getSongDetails(itemTitle))
		print(newsong_titles)
		return newsong_titles

	def getSongDetails(self,song):
		#Cuts out the uneeded paranthesis from the songs 
		if '(' in song:
			index = song.find('(')
			newsong = song[:index]
			return newsong
		else:
			return song

	def transferPlaylistToSpotify(self):
		#Initiates transfer of playlist to spotify
		newsong_title = []
		playlists = {}
		req  = self.youtube.playlists().list(part = 'snippet', mine = True)
		res =  req.execute()
		items = res['items']
		for item in items:
			playlists[item['snippet']['title']] = item['id']
		print("Choose a playlist to transfer to Spotify:")
		flag = True
		while flag:
			for playlist in playlists:
				print(playlist)
			x = input("Enter the name of the playlist as you see above (Case Sensitive): ")
			if x in playlists:
				newsong_titles = self.getUserPlaylistSongs(playlists[x])
				flag = False
			else:
				print("Cannot find the playlist titled: "+ x)
		return newsong_titles





if __name__ == '__main__':
	yt = YoutubeAPI()
	yt.getUserPlaylistSongs(proj_keys.playlist_id)

