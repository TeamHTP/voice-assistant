import os
import praw
from random import randint
from src import text_to_speech as tts
from src.skills.skill import Skill
from src.skills.skills import register


reddit = praw.Reddit(
            client_id=os.getenv('CLIENTID'),
            client_secret=os.getenv('CLIENTSECRET'),
            user_agent=os.getenv('USER')
            )


@register
class Pasta(Skill):
    primary_triggers = ['pasta']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.post_ids = []
        self.limit = 50
        for submission in reddit.subreddit("copypasta").hot(limit=self.limit):         
            self.post_ids.append(submission.id)

    def do(self, params):
        post_data = reddit.submission(id=self.post_ids[randint(0, self.limit)])
        text = post_data.selftext.replace('\n\n', ' ').replace('\n', '')
        tts.say(text)
