import time
from src import text_to_speech as tts
from src.skills.skill import Skill
from src.skills.skills import register


@register
class Timer(Skill):
    primary_triggers = ['start', 'stop']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.started = False
        self.time = 0

    def do(self, params):
        if not self.started:
            self.started = True
            self.time = time.time()
            tts.say('timer started')
        else:
            self.started = False
            self.time = str(round((time.time() - self.time), 2))
            temp_str = 'the timer stop. time was ' + self.time + ' seconds'
            self.time = 0
            tts.say(temp_str)
