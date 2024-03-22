import os


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id
        self.channel_data = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_data['items'][0]['snippet']['title']
        self.description = self.channel_data['items'][0]['snippet']['description']
        self.url = "https://www.youtube.com/channel/UCZ_B-KkMbNAsax9H6ohFTqw"

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return print(channel)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.}"

    @property
    def channel_id(self):
        return self._channel_id