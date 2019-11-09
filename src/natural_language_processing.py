import nltk
import spacy
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

nlp = spacy.load('en_core_web_sm')


def text_to_token(input_str):
    docs = nlp(input_str)
    for word in docs:
        print(word.text, word.pos_)
        