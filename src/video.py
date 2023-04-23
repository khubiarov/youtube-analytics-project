from googleapiclient.discovery import build

import os


class Video:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.video_id = video_id
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=video_id
                                                         ).execute()

        self.title = self.video_response['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/watch?v={self.video_id}'
        self.viewCount = self.video_response['items'][0]['statistics']["viewCount"]
        self.likecount = self.video_response['items'][0]['statistics']["likeCount"]

    def __str__(self):
        return self.title

class PLVideo(Video):


    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist
        self.playlist = self.youtube.playlistItems().list(playlistId=self.id_playlist,
                                               part='contentDetails',
                                               maxResults=50,
                                               ).execute()
        self.pl_list = self.playlist['items']
        i = 0
        for video in self.pl_list:

            if video['contentDetails']['videoId'] == self.video_id:
                self.id_playlist = video['id']

    def __str__(self):
        return self.title