import nltk
import spacy
from nltk.corpus import state_union, wordnet
from nltk.tokenize import PunktSentenceTokenizer
from src.skills.time import Time
from src.skills.weather import Weather
# from src.skills.broken_translate import BrokenTranslate
from src.skills.joke import Joke

nlp = spacy.load('en_core_web_sm')

evalulate_next_input = False

weather_skill = Weather()

SKILLS = {
    'time': Time().do,
    'weather': weather_skill.do,
    'low_temperature': weather_skill.do,
    'rain': weather_skill.do,
    'snow': weather_skill.do,
    'sunny': weather_skill.do,
#    'translate': BrokenTranslate().do,
    'joke': Joke().do
}


def text_to_token(input_str):
    global evalulate_next_input
    docs = nlp(input_str)
    entities=[(i, i.label_, i.label) for i in docs.ents]
    for ent in entities:
        print(ent)
    asking_oracle = evalulate_next_input
    evalulated = False
    synonyms_list = []
    for word in docs:
        print(word.text, word.pos_)
        syns = wordnet.synsets(word.text)
        print(f'{word.text.upper()}')
        if not asking_oracle:
            if word.text == 'oracle':
                asking_oracle = True
        for syn in syns:
            print(f'{syn.name()}: {syn.lemma_names()}')
            for lemma_sym in syn.lemma_names():
                if not lemma_sym in synonyms_list:
                    synonyms_list.append(lemma_sym)
                if asking_oracle:
                    if lemma_sym in SKILLS:
                        SKILLS[lemma_sym](docs)
                        evalulated = True
                        evalulate_next_input = False
                        return

    if asking_oracle and not evalulated and not evalulate_next_input:
        evalulate_next_input = True
        print("Next sentence will be evaluated")
