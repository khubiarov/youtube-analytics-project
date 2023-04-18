import json
import os


from googleapiclient.discovery import build

#import isodate

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.about_channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.about_channel['items'][0]['snippet']['title']
        self.description = self.about_channel['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriberCount = self.about_channel['items'][0]['statistics']["subscriberCount"]
        self.video_count = self.about_channel['items'][0]['statistics']['videoCount']
        self.viewCount = self.about_channel['items'][0]['statistics']["viewCount"]

    def print_info(self) -> None:
        """Returns info about channel, I have deleted excess method, and excess request of API"""



        return(json.dumps(self.about_channel, indent=2, ensure_ascii=False))


# I don't know how to test next two methods, becouse they return nothing
    @classmethod
    def get_service(cls):
        '''Returns youtube's class copy, if I got it right'''
        return cls.youtube

    def to_json(self, file_name):
        '''creates file with JSON-structure about of requested channel'''
        with open(file_name, "wt") as file:

            file.write(json.dumps(self.about_channel))

    def __str__(self):
        '''returns Name of channel and url'''
        return f'{self.title} ({self.url})'

# methodes after this line for work with calculate of subscribes
    def __add__(self, other):
        '''calculates subscribers of both channel'''
        return int(self.subscriberCount) + int(other.subscriberCount)

    def __sub__(self, other):
        return int(self.subscriberCount) - int(other.subscriberCount)

    def __lt__(self, other):
        return int(self.subscriberCount) < int(other.subscriberCount)

    def __gt__(self, other):
        return int(self.subscriberCount) > int(other.subscriberCount)

    def __le__(self, other):
        return int(self.subscriberCount) <= int(other.subscriberCount)

    def __ge__(self, other):
        return int(self.subscriberCount) >= int(other.subscriberCount)