import os, json, vlc, pafy, time
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

class PlayMusic:
    def __init__(self):
        keyFile = open('key.txt', 'r')
        if keyFile.mode == 'r':
            self.key = keyFile.read()
        assert self.key
        print(self.key)
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
            order="viewCount",
            q=song,
            type="video"
        )

        response = request.execute()

        res = {
            "videoId": response["items"][0]['id']['videoId'],
            "title": response["items"][0]['snippet']['title'],
            "channel": response["items"][0]['snippet']['channelTitle']
        }

        extraInfo = youtube.videos().list(
            part='contentDetails',
            id=res['videoId'],
            fields='items'
        )

        rawDuration = extraInfo.execute()['items'][0]['contentDetails']['duration']
        m = rawDuration.find('M')
        s = rawDuration.find('S')
        minute = rawDuration[m - 1: m]
        second = rawDuration[s - 2: s]
        res['duration'] = int(minute) * 60 + int(second)

        
        youtubeUrl = self.url + res['videoId']
        vidUrl = pafy.new(youtubeUrl).getbest().url
        self.media = vlc.MediaPlayer(vidUrl)
        self.media.play()
        print (self.media.get_state())
	
        print (res)
        return res

    def stop(self):
	    self.media.stop()
        
r = PlayMusic().play("sparks fly")
time.sleep(r['duration'])