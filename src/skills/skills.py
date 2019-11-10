import sys


registry = {}


def register(skill):
    def wrapper():
        for word in skill.primary_triggers:
            if word not in registry.keys():
                registry[word] = skill
            else:
                print(f'Skill: {type(skill).__name__} not registered for word: {word}, due to conflict.', file=sys.stderr)
