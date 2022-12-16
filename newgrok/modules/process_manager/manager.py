import shutil
import atexit
import time
import json
import os
import subprocess
import datetime

import requests
from requests.exceptions import ConnectionError

from ..telegram.bot import BotTelegram

class Manager:
    ngrok_api = 'http://localhost:4040/api/tunnels'
    process = None

    def __init__(self, port: int, protocol: str, chat_id: str, bot_token: str) -> None:
        if not shutil.which('ngrok'):
            print('is ngrok installed?')
            os._exit(0)
        self.port = port
        self.protocol = protocol
        self.chat_id = chat_id
        self.bot_token = bot_token

    def run(self):
        end_time = self.__get_restart_hour()
        while True:
            if self.process == None or end_time < datetime.datetime.now():
                self.__up_process()

    def __get_restart_hour(self) -> datetime.datetime:
        ngrok_start = datetime.datetime.now()
        ngrok_end = ngrok_start + datetime.timedelta(hours=1.5)
        return ngrok_end

    def __up_process(self):
        self.__stop_ngrok()
        self.process = subprocess.Popen(
            ['ngrok', 'http', '--inspect=false', str(self.port)],
            stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
        )
        self.__send_new_url()
        self.__register_quit_ngrok_process(self.process.terminate)

    def __stop_ngrok(self) -> None:
        if self.process != None:
            self.process.terminate()

    def __register_quit_ngrok_process(self, func: callable) -> None:
        atexit._clear()
        atexit.register(func)

    def __get_public_url(self) -> str:
        attempts = 10
        for attempt in range(attempts):
            try:
                response = requests.get(self.ngrok_api)
                break
            except ConnectionError:
                time.sleep(2)
            if attempt >= attempts -1:
                print('is ngrok running?')
                os._exit(0)
        data = response.text
        tunnel_url = json.loads(data)['tunnels'][0]['public_url']
        return tunnel_url

    def __send_new_url(self):
        url = self.__get_public_url()
        bot = BotTelegram(self.chat_id, self.bot_token)
        bot.send_new_url(url)