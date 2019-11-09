import nltk
import spacy
from nltk.corpus import state_union, wordnet
from nltk.tokenize import PunktSentenceTokenizer
from src.skills.time import Time

nlp = spacy.load('en_core_web_sm')

evalulate_next_input = False

SKILLS = {
  'time': Time().do
}


def text_to_token(input_str):
    global evalulate_next_input
    docs = nlp(input_str)
    entities=[(i, i.label_, i.label) for i in docs.ents]
    for ent in entities:
        print(ent)
    asking_oracle = evalulate_next_input
    evalulated = False
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
                if asking_oracle:
                    if word.text in SKILLS:
                        SKILLS[word.text](docs)
                        evalulated = True
                        evalulate_next_input = False
                        return
    if asking_oracle and not evalulated:
        evalulate_next_input = True
        print("Next sentence will be evaluated")