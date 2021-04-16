import configparser

import telebot
import requests
from bs4 import BeautifulSoup as bea

config = configparser.ConfigParser()
config.read( 'set.ini' )

bot = telebot.TeleBot(config ['bot'] ['token'] )

@bot.message_handler(commands = ['start'])
def comm_message(message):
    if message.text == '/start':
        bot.send_message(message.chat.id,' Привет ')
        
@bot.message_handler(content_types = ['text'])
def site_message(message):
    if message.text == 'новость':
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        s = requests.get('https://kanobu.ru/tags/steam/',  headers = headers)
        html = bea(s.content, 'html.parser')
        tmp = html.find_all('a', attrs = {'class' : 'aQ_hk'})
        for i in tmp:
            bot.send_message(message.chat.id, 'https://kanobu.ru' + i['href'] )
            
bot.polling(none_stop=True, interval = 0)
