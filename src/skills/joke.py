from src import text_to_speech as tts
import requests
import time


class Joke:

    def do(self, params):
        response = requests.get('https://official-joke-api.appspot.com/jokes/random')
        if response.status_code == 200 && response.headers['content-type'] == 'application/json':
            json = response.json()
            setup = json['setup']
            punchline = json['punchline']

            tts.say(setup)
            time.sleep(0.5)
            tts.say(punchline)
