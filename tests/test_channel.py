import pytest
from src.channel import Channel

@pytest.fixture


def test_channel():
    return Channel('UC5dgoavpIertLkNDDITDoBQ')



def test_channel_as(test_channel):
    test_channel.print_info() == """{
  "kind": "youtube#channelListResponse",
  "etag": "K1u1grr8DnmhlECR3L7fMsmeCTY",
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#channel",
      "etag": "b4bsorFV7e7Hwi7R6e1e-wXeYGM",
      "id": "UC5dgoavpIertLkNDDITDoBQ",
      "snippet": {
        "title": "Дмитрий Бачило",
        "description": "Этот канал в основном посвящен обзорам всякого старого железа и софта, впрочем не только старого.",
        "customUrl": "@bachilodmitry",
        "publishedAt": "2007-02-11T15:05:30Z",
        "thumbnails": {
          "default": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJUWr9_UmIP7UaXnZD1bvxwi0RPr_jYVFVNGNRAXUw=s88-c-k-c0x00ffffff-no-rj",
            "width": 88,
            "height": 88
          },
          "medium": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJUWr9_UmIP7UaXnZD1bvxwi0RPr_jYVFVNGNRAXUw=s240-c-k-c0x00ffffff-no-rj",
            "width": 240,
            "height": 240
          },
          "high": {
            "url": "https://yt3.ggpht.com/ytc/AL5GRJUWr9_UmIP7UaXnZD1bvxwi0RPr_jYVFVNGNRAXUw=s800-c-k-c0x00ffffff-no-rj",
            "width": 800,
            "height": 800
          }
        },
        "localized": {
          "title": "Дмитрий Бачило",
          "description": "Этот канал в основном посвящен обзорам всякого старого железа и софта, впрочем не только старого."
        }
      },
      "statistics": {
        "viewCount": "18029643",
        "subscriberCount": "130000",
        "hiddenSubscriberCount": false,
        "videoCount": "265"
      }
    }
  ]
}"""

