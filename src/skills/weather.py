from src.skills.skill import Skill
from src import text_to_speech as tts
import os
from src import location
import pyowm
from src.skills.skills import register

OPEN_WEATHER_KEY = os.getenv('OPEN_WEATHER_KEY')

owm = pyowm.OWM(OPEN_WEATHER_KEY)


@register
class Weather(Skill):

    primary_triggers = ['weather']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def do(self, params):
        thread = self.use_open_weather(OPEN_WEATHER_KEY)


    def get_confidence(self, synonyms, spoken):
        confidence = 0
        outdoors_in_syn = 'outdoors' in synonyms
        exist_in_syn = 'exist' in synonyms
        if outdoors_in_syn or exist_in_syn:
            if 'cold' in synonyms:
                confidence += 0.9
            elif 'hot' in synonyms:
                confidence += 0.9
            elif 'snow' in synonyms:
                confidence += 0.9
            elif 'rain' in synonyms:
                confidence += 0.9
            elif 'cloudy' in synonyms:
                confidence += 0.9
        if outdoors_in_syn and exist_in_syn:
            confidence += 0.5
            if 'good' in synonyms:
                confidence += 0.4
            elif 'bad' in synonyms:
                confidence += 0.4
        if ('weather' in synonyms or 'whether' in spoken or 'wether' in spoken) and 'what' in synonyms:
            confidence += 0.9
        return confidence


    def use_open_weather(self, api_key):
        global owm
        loc_data = location.get_location()
        weather = owm.weather_at_coords(float(loc_data.latitude), float(loc_data.longitude)).get_weather()
        print(weather)
        tts.say(f'It is currently {weather.get_status()} with a temperature of {round(weather.get_temperature("fahrenheit")["temp"])} degrees fahrenheit')
        return
