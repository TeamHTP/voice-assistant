import nltk
import spacy
from nltk.corpus import state_union, wordnet
from nltk.tokenize import PunktSentenceTokenizer
from src.skills.time import Time

nlp = spacy.load('en_core_web_sm')

SKILLS = {
  'time': Time().do
}


def text_to_token(input_str):
    docs = nlp(input_str)
    entities=[(i, i.label_, i.label) for i in docs.ents]
    for ent in entities:
        print(ent)
    for word in docs:
        print(word.text, word.pos_)
        syns = wordnet.synsets(word.text)
        print(f'{word.text.upper()}')
        for syn in syns:
            print(f'{syn.name()}: {syn.lemma_names()}')
        if word.text in SKILLS:
          SKILLS[word.text](docs)
