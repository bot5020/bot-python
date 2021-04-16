# bot-python
Хай! config = configparser.ConfigParser() 
config.read( 'set.ini' ) он считывает файл "set.ini"
bot = telebot.TeleBot(config ['bot'] ['token'] ) он задает переменной значенние токена 
