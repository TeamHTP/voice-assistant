from src import text_to_speech as tts
from src.skills.skills import register


@register
class Cat:

    primary_triggers = ['cat']

    def do(self, params):
        words = map(lambda word: word.text, params[1:])
        tts.say(' '.join(words))

    def get_confidence(self, synonyms, spoken):
        if spoken:
            if spoken[0] == 'cat' or spoken[0] == 'tat':
                return 1
        return 0
