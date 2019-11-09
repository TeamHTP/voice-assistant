from googletrans import Translator
from src.skills.skill import Skill
from src import text_to_speech as tts


class BrokenTranslate(Skill):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.translator = Translator()


    def do(self, params):
        tts.say('The time is ' + datetime.now().strftime('%I:%M %p'))
