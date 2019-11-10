import nltk
import spacy
from nltk.corpus import state_union, wordnet
from nltk.tokenize import PunktSentenceTokenizer
from src.skills import skills

nlp = spacy.load('en_core_web_sm')

evalulate_next_input = False

def text_to_token(input_str):
    global evalulate_next_input
    docs = nlp(input_str)
    entities=[(i, i.label_, i.label) for i in docs.ents]
    for ent in entities:
        print(ent)
    asking_oracle = evalulate_next_input
    evalulated = False
    evalulate_next_input = False
    heard_oracle = False
    synonyms_list = []
    i = 0
    for word in docs:
        # print(word.text, word.pos_)
        syns = wordnet.synsets(word.text)
        # print(f'{word.text.upper()}')
        if not asking_oracle:
            if word.text == 'oracle' or word.text == 'oricle' or word.text == 'oricl' or word.text == 'oracol' or word.text == 'eyoricle' or word.text == 'orical' or word.text == 'orcal':
                asking_oracle = True
                heard_oracle = True

        if asking_oracle:
            for syn in syns:
                print(f'{syn.name()}: {syn.lemma_names()}')

                for lemma_sym in syn.lemma_names():
                    if not lemma_sym in synonyms_list:
                        synonyms_list.append(lemma_sym)
                    if asking_oracle:
                        if lemma_sym in skills.registry:
                            skills.registry[lemma_sym].do(docs[i:])
                            evalulated = True
                            return

    if heard_oracle and not evalulated:
        evalulate_next_input = True
        print("Next sentence will be evaluated")
