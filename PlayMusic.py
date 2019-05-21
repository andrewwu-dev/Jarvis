import vlc, pafy
import googleapiclient.discovery

class PlayMusic:
    def __init__(self):
        keyFile = open('youtubeKey.txt', 'r')
        if keyFile.mode == 'r':
            self.key = keyFile.read()
        assert self.key
        self.url = "https://www.youtube.com/watch?v="
        self.media = None
        
    def play(self, song):
        api_service_name = "youtube"
        api_version = "v3"

        # Create an API client
        youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = self.key)

        request = youtube.search().list(
            part="snippet",
            maxResults=1,
            order="relevance",
            q=song,
            type="video"
        )

        response = request.execute()

        res = {
            "videoId": response["items"][0]['id']['videoId'],
            "title": response["items"][0]['snippet']['title'],
            "channel": response["items"][0]['snippet']['channelTitle']
        }
        
        youtubeUrl = self.url + res['videoId']
        vidUrl = pafy.new(youtubeUrl).getbest().url
        self.media = vlc.MediaPlayer(vidUrl)
        print (res)
        self.media.play()
        return res

    def stop(self):
	    self.media.stop()