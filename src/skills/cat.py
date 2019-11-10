from src import text_to_speech as tts
from src.skills.skills import register


@register
class Cat:

    primary_triggers = ['cat']

    def do(self, params):
        words = map(lambda word: word.text, params)
        tts.say(' '.join(words))

    def get_confidence(self, synonyms, spoken):
        if spoken[1] == 'cat':
            return 1
        return 0
