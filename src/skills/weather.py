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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def do(self, params):
        self.use_open_weather(OPEN_WEATHER_KEY)


    def use_open_weather(self, api_key):
        global owm
        loc_data = location.get_location()
        weather = owm.weather_at_coords(float(loc_data.latitude), float(loc_data.longitude)).get_weather()
        print(weather)
        tts.say(f'It is currently {weather.get_status()} with a temperature of {round(weather.get_temperature("fahrenheit")["temp"])} degrees fahrenheit')
        return
