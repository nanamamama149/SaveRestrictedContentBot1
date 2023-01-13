#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("18601774", default=None, cast=int)
API_HASH = config("218ada48a21b6a605f3123022d85974a", default=None)
BOT_TOKEN = config("5785290597:AAFytyekZj9s93cjuaKDyFwo33PGQYfbuRA", default=None)
SESSION = config("BQEb1y4AlWF5VcsmhfqUb7S3wwD5d5ZyQk4NAX6KUj_wsoK2gpkbvxNLXlMV89UYZFwDZrpZgMIQ4RuMFO-aSkey97--t3PQIZIhVawF1NsEXEfJv9VLjWRZiZHWQ1JUouliPkerEqKspRI0URAtz2-lSDq2mI1qdoIDv0paEwX2Zxq2GQLY9R8gMbw8qmN_oxBBQjcwXS-OlDl4Nh7XECTUk010FWBGQbZb5Bx7SDqqoZyaIwzujcFPaYyps0zw0fZltlzxgayLQbbfaXAmv84eoW-ubBTEKRSUuQD5hwOc_VqOHXY2iAVzZzUmcnJMuxyM4sYNcz1qI3aruzAmdfRcfmRJrQAAAABGexBPAA", default=None)
FORCESUB = config("https://t.me/+4zuY__2ON344ODFh", default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
