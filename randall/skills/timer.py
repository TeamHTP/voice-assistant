import time
from randall import text_to_speech as tts
from randall.skills.skill import Skill
from randall.skills_registry import register


@register
class Timer(Skill):
    primary_triggers = ['start']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.started = False
        self.time = 0

    def do(self, params):
        if not self.started:
            for word in params:
                if word.text == 'start':
                    self.started = True
                    self.time = time.time()
                    tts.say('timer started')
        else:
            for word in params:
                if word.text == 'stop':
                    self.started = False
                    self.time = str(round((time.time() - self.time), 2))
                    temp_str = 'the timer stop. time was ' + self.time + ' seconds'
                    self.time = 0
                    tts.say(temp_str)

    def get_confidence(self, synonyms, spoken):
        if 'timer' in synonyms or 'start' in synonyms or ('timer' in synonyms and 'stop' in synonyms):
            return 1
        else:
            return 0
