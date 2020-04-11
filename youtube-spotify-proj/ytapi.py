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

