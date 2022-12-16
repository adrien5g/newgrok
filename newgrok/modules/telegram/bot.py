import telebot

class BotTelegram:

    def __init__(self, chat_id, bot_id):
        self.chat_id = chat_id
        self.bot_id = bot_id

    def send_new_url(self, url: str) -> bool:
        try:
            bot = telebot.TeleBot(self.bot_id)
        except:
            return False

        bot.send_message(self.chat_id, f'🦆 New url - {url}')
        return True
    