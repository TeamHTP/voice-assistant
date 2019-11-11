from randall import text_to_speech as tts
import requests
import time
from randall.skills_registry import register


@register
class Joke:

    primary_triggers = ['joke']

    def do(self, params):
        response = requests.get('https://official-joke-api.appspot.com/jokes/random')
        if response.status_code == 200 and response.headers['content-type'] == 'application/json; charset=utf-8':
            json = response.json()
            setup = json['setup']
            punchline = json['punchline']

            tts.say(setup)
            time.sleep(0.5)
            tts.say(punchline)


    def get_confidence(self, synonyms, spoken):
        if 'say' in synonyms and 'joke' in synonyms:
            return 1
        return 0