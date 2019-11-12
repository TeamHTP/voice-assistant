import sys

registry = {}


def register(skill):
    skill_instance = skill()
    for word in skill_instance.primary_triggers:
        if word not in registry:
            registry[word] = skill_instance
            print(f'Skill: {type(skill_instance).__name__} registered for word: {word}.')
        else:
            print(f'Skill: {type(skill_instance).__name__} not registered for word: {word}, due to conflict.', file=sys.stderr)
    return skill_instance

# Importing the skills will invoke @register
from randall.skills import joke
from randall.skills import kill
from randall.skills import time
from randall.skills import timer
from randall.skills import weather
from randall.skills import hello
from randall.skills import ping
from randall.skills import cat
from randall.skills import wikipedia