from src import text_to_speech as tts
from src.skills.skills import register


@register
class Ping:

    primary_triggers = ['ping']

    def do(self, params):
        tts.say('pong');

    def get_confidence(self, synonyms, spoken):
        if 'ping' in spoken:
            return 1
        return 0
