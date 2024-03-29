import nltk
import spacy
import time
from nltk.corpus import state_union, wordnet
from nltk.tokenize import PunktSentenceTokenizer
from src.skills import skills
from src import ws_client

nlp = spacy.load('en_core_web_sm')

evalulate_next_input = False
last_heard_oracle = time.time()
names = [
    'randall',
    'randal',
    'erandel',
    'randel',
    'erandom',
    'randl',
    'rendel',
    'randol',
    'randle',
    'rendole',
    'randole'
]

def text_to_token(input_str):
    global evalulate_next_input
    global names
    global last_heard_oracle
    docs = nlp(input_str)
    entities=[(i, i.label_, i.label) for i in docs.ents]
    # for ent in entities:
        # print(ent)
    asking_oracle = evalulate_next_input and time.time() - last_heard_oracle < 10
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
            if word.text in names:
                asking_oracle = True
                heard_oracle = True
                ws_client.send_start()
            i += 1

        if asking_oracle:
            for syn in syns:
                # print(f'{syn.name()}: {syn.lemma_names()}')

                for lemma_sym in syn.lemma_names():
                    if not lemma_sym in synonyms_list:
                        synonyms_list.append(lemma_sym)

    if asking_oracle:
        print("Recognized: %s" % input_str)
        words = [word.text for word in docs[i:]]
        highest_conf_skill = get_highest_confidence_skill(synonyms_list, words)
        if highest_conf_skill:
            highest_conf_skill.do(docs[i:])
            ws_client.send_stop()
            return

    if heard_oracle and not evalulated:
        evalulate_next_input = True
        last_heard_oracle = time.time()
        print("Next sentence will be evaluated")
    elif not evalulated:
        ws_client.send_stop()


def get_highest_confidence_skill(synonyms_list, spoken_list):
    highest_conf = 0
    conf_skill = None
    for primary_trigger, skill in skills.registry.items():
        skill_conf = skill.get_confidence(synonyms_list, spoken_list)
        print(f'Confidence in {type(skill).__name__}: {skill_conf}')
        if skill_conf > highest_conf:
            highest_conf = skill_conf
            conf_skill = skill
    return conf_skill