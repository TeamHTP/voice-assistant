from src.skills.skill import Skill
from src import text_to_speech as tts
from datetime import datetime
from src.skills.skills import register

@register
class Time(Skill):

    primary_triggers = ['time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def do(self, params):
        tts.say('The time is ' + datetime.now().strftime('%I:%M %p'))


    def get_confidence(self, synonyms, spoken):
        if 'time' in synonyms:
            return 1
        else:
            return 0