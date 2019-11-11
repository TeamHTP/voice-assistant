import os
import praw
from random import randint
from randall import text_to_speech as tts
from randall.skills.skill import Skill
from randall.skills.skills import register


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
        
        text = 'What the jiminy crickets did you just flaming say about me, you little bozo? I’ll have you know I graduated top of my class in the Cub Scouts, and I’ve been involved in numerous secret camping trips in Wyoming, and I have over 300 confirmed knots. I am trained in first aid and I’m the top bandager in the entire US Boy Scouts (of America). You are nothing to me but just another friendly face. I will clean your wounds for you with precision the likes of which has never been seen before on this annual trip, mark my words. You think you can get away with saying those shenanigans to me over the Internet? Think again, finkle. As we speak I am contacting my secret network of MSN friends across the USA and your IP is being traced right now so you better prepare for the seminars, man. The storm that wipes out the pathetic little thing you call your bake sale. You’re frigging done, kid. I can be anywhere, anytime, and I can tie knots in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in road safety, but I have access to the entire manual of the United States Boy Scouts (of America) and I will use it to its full extent to train your miserable butt on the facts of the continents, you little schmuck. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your silly tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goshdarned sillyhead. I will throw leaves all over you and you will dance in them. You’re friggin done, kiddo.'

        tts.say(text)

    def get_confidence(self, synonyms, spoken):
        if ('pasta' in synonyms or 'possof' in spoken or 'posta' in spoken or 'possta' in spoken 
         or 'paster' in spoken or 'possa' in spoken or 'postta' in spoken or 'pose' in spoken 
         or 'posstu' in spoken or 'posto' in spoken or 'posito' in spoken or 'possitar' in spoken
         or 'poster' in spoken or 'postita' in spoken or 'pusta' in spoken or 'possitle' in spoken):
            return 1
        else:
            return 0
