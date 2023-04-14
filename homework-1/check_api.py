import json

from src.channel import Channel

channel1 = Channel("UC5dgoavpIertLkNDDITDoBQ")
print(channel1.print_info())
print(channel1.about_channel)
print(channel1.about_channel['items'][0]['snippet']['thumbnails']['default']['url'])