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

from src.skills import pasta
from src.skills import joke
from src.skills import kill
from src.skills import time
from src.skills import timer
from src.skills import weather
from src.skills import hello
