import time
from src import text_to_speech as tts
from src.skills.skill import Skill
from src.skills.skills import register


@register
class Kill(Skill):
    primary_triggers = ['kill']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do(self, params):
        tts.kill()

    def get_confidence(self, synonyms, spoken):
        if ('stop' in synonyms or 'kill' in synonyms or 'kell' in spoken or 'killed' in spoken or 'killd' in spoken) and 'timer' not in synonyms:
            return 1
        else:
            return 0
