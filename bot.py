import telebot
from pytube import YouTube as yt
import telegraph
bot = telebot.TeleBot('986722664:AAEx7v_gw8gZvKS7VEZojP2P5JdKfBmoOEQ')
bot.send_message(120929625, 'test')
a = yt('https://www.youtube.com/watch?v=5X5ZLWdAnt4').streams[2].download()
# print(a)
f = open('19 Уроки React JS (route browser-router маршрутизация) - react курсы бесплатно.mp4', 'rb')
# m = telegraph.upload.upload_file(f.read())
bot.send_video(120929625, f.read(), supports_streaming=True)
bot.send_message(120929625, 'всё')
