import json
import os


from googleapiclient.discovery import build

import isodate








class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.about_channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.about_channel['items'][0]['snippet']['title']
        self.video_count = self.about_channel['items'][0]['statistics']['videoCount']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале.Убрал лишнюю функцию лишний вызов апи"""



        return(json.dumps(self.about_channel, indent=2, ensure_ascii=False))



    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, file_name):
        with open(file_name, "wt") as file:

            file.write(json.dumps(self.about_channel))


