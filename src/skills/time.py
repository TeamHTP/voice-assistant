from src.skills.skill import Skill
import time


class Time(Skill):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
    def do(self, params):
        print(time.time())