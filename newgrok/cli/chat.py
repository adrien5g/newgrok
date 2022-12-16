import os
import telebot
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = telebot.TeleBot(os.getenv('bot_token'))

@bot.message_handler(commands=['start'])
def greet(message):
	bot.reply_to(message, f'Chat Id = {message.chat.id}')
	show_chat_id(message)

@bot.message_handler(func=lambda message: True)
def response(message):
	bot.reply_to(message, f'Chat Id = {message.chat.id}')
	show_chat_id(message)

def show_chat_id(message):
	print(f'Chat Id = {message.chat.id}')
	os._exit(0)

def get_chat_id():
	print('Send a message to your bot.')
	bot.infinity_polling()
