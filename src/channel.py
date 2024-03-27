import json
import os
from googleapiclient.discovery import build

'''Клонировал проект'''

import isodate


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.url = "https://www.youtube.com/channel/UCZ_B-KkMbNAsax9H6ohFTqw"
        self.channel_info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.channel_info["items"][0]["id"]}'
        self.subs = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.views = self.channel_info['items'][0]['statistics']['viewCount']

        self.__service = self.youtube

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        channel_info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel_info, indent=2, ensure_ascii=False))

    '''
    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return print(channel)
    '''

    def to_json(self, filename):
        """Cохраняет в файл значения атрибутов экземпляра `Channel`"""
        channel_data = {
            "channel_id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriber_count": self.subs,
            "video_count": self.video_count,
            "view_count": self.views
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(channel_data, file, indent=4, ensure_ascii=False)
