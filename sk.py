import time
from skpy import Skype
from decouple import config
from datetime import datetime, date
from bdateutil import isbday


while True:
    now = datetime.now()
    if now.strftime("%H:%M") == "10:00" and isbday(date(now.year, now.month, now.day)):
        user = Skype(config('SK_LOGIN'), config('SK_PASS'))
        user.chats(config['SK_CHAT_ID']).sendMsg("Hello guys")
    time.sleep(60)
