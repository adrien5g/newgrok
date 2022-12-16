from os import getenv

from .modules.process_manager.manager import Manager
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Newgrok:

    def __init__(self) -> None:
        port = getenv('app_port')
        chat_id = getenv('chat_id')
        bot_token = getenv('bot_token')
        protocol = getenv('protocol')
        self.manager = Manager(port, protocol, chat_id, bot_token)

    def run(self):
        self.manager.run()