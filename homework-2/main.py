from src.channel import Channel

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # получаем значения атрибутов
    print(moscowpython.name)  # MoscowPython
    print(moscowpython.video_count)  # 685 (может уже больше)
    print(moscowpython.url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A

    print(f'channel id: {moscowpython.channel_id}')
    print(f'channel name: {moscowpython.name}')
    print(f'channel description: {moscowpython.description}')
    print(f'channel url: {moscowpython.url}')
    print(f'subscribers count: {moscowpython.subscriber_count}')
    print(f'video count: {moscowpython.video_count}')
    print(f'views count: {moscowpython.view_count}')

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())

    # создаем файл 'moscowpython.json' c данными по каналу
    moscowpython.to_json('moscowpython.json')