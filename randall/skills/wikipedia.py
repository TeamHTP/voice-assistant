from randall import text_to_speech as tts
import requests
import time
from randall.skills.skills import register


@register
class Wikipedia:

    primary_triggers = ['wikipedia']

    def do(self, params):
        words = [word.text for word in params[1:]]
        term = 0
        i = 0
        for word in words:
            if word == 'what\'s':
                term = i
            elif word == 'a':
                term = i
            elif word == 'an':
                term = i
            elif word == 'is':
                term = i
            elif word == 'the':
                term = i
            i+= 1
        query = ' '.join(words[term + 1:])
        print(f'https://en.wikipedia.org/w/api.php?action=opensearch&search={query}&limit=1&namespace=0&format=json')
        response = requests.get(f'https://en.wikipedia.org/w/api.php?action=opensearch&search={query}&limit=1&namespace=0&format=json')
        if response.status_code == 200 and response.headers['content-type'] == 'application/json; charset=utf-8':
            json = response.json()
            if len(json) >= 2 and isinstance(json[2], list) and len(json[2]) >= 1:
              tts.say(json[2][0])


    def get_confidence(self, synonyms, spoken):
        confidence = 0
        if ('what' in spoken or 'what\'s' in spoken):
            confidence += 0.25
        if 'exist' in synonyms:
            confidence += 0.25
        return confidence