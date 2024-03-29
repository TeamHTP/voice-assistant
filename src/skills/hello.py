from src import text_to_speech as tts
from src.skills.skills import register


@register
class Hello:

    primary_triggers = ['hello']

    def do(self, params):
        tts.say('Hello, world!');

    def get_confidence(self, synonyms, spoken):
        if 'hello' in spoken:
            return 1
        return 0
