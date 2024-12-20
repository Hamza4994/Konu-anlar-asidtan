import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "28503231"))
API_HASH = getenv("API_HASH", "3f4f8597a1a8cfdd975eec20278c28b6")
BOT_TOKEN = getenv("BOT_TOKEN", "6037979897:AAEHGPBYwswfjwVX7IM_qO5-K_ylILlOHAk")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Kingbrukh:kingkhan@kingbruh.ra3pjgm.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 500))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002028213552"))
OWNER_ID = int(getenv("OWNER_ID", 6076070444))
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/hamza49490/konusanlaar-asistan",
)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/askkoleji")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/konnusanlar")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
STRING1 = getenv("STRING_SESSION", "AgCidfH6I_WUMkIAkzOGqAoVCH0mBHU1vvkcmXQoPJ6Z3XQst9_3qX6g9TjjNTnDh80swCH5DSPfxxq34bn_8bQbNyYlyqNg0F6j5vEhdwm5vrgeOhpqrkXOVEyu7zofKKxsVHJFTxcUZ9RZXhR3t68q1-4JG1LkLpSYOCg1VsxtJW7VXGrBSz7U4moynHIKgrrHN6DsaLKIxwgZ0_FM9USIEN6kEFf16ea-V3UmqWArXkrE0GZHmiO9NhdRt8IC9JIIXPjhSQxYGiN7PZzcmEnoJ1MJ4kcHCjdFN4fOZZ1RMEsGV-3zqpliWyIPM_xayfUczrlEwa-J_T9Z9ABNlsSLAAAAAcvtzKAA")
STRING2 = getenv("STRING_SESSION2", "BAGy7L8Aeg8PsfiJ5bOWfkbVIgbiuV4gtJPTFXolWZvRx8VnXXE0NHUM8hpZYgs1lKxC_j3_aFr17Th3U2CjXRcTg_IqrlhdnkUfbUPbH8J6s-xRI_ElMzGty0DI7n81b5kUy8ADZlw8vUYjEGVlSddr6oQoXjN2qKTBwF3tIs8_U0n4lY8yD3T4iGfpZova5cSGLD4ikfMdTJ1WW0kCacofilRnV4IL6RysulV9AJfoxG3QHTbCXBiwpjJ7PDDcmOzYPAQqVgHUbZmFzrhwuh1rdkCqcLzQPy0WsSABeFaI6S-xe4mpUotmYJT6tnsoKQysg0mxXsYhiZCbMEpLjWg5Ft679AAAAAG0snY0AA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)
# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/5933c1352e77e43c7af52.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
