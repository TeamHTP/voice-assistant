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
