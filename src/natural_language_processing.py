import nltk
import spacy
from nltk.corpus import state_union, wordnet
from nltk.tokenize import PunktSentenceTokenizer
from src.skills import skills

nlp = spacy.load('en_core_web_sm')

evalulate_next_input = False
jeffrey = [
    'jeffrey',
    'jefffrey',
    'jeffre',
    'jeoffrey',
    'jefferey',
    'cheffrey',
    'geffrey',
    'geffry',
    'ajeffrey',
    'geoffrey',
    'heffrey',
    'chefferey',
    'jeffry',
    'ajeofry',
    'jeoprey',
    'effrey',
    'jeofary',
    'jeofrey',
    'adjeffrey',
    'jeopry',
    'joffri',
    'joffrey',
    'jowferey',
    'jopfery',
    'joffry',
    'jofferey',
    'jofring',
    'afree',
    'geofrey',
    'geofry'
]

def text_to_token(input_str):
    global evalulate_next_input
    global jeffrey
    docs = nlp(input_str)
    entities=[(i, i.label_, i.label) for i in docs.ents]
    # for ent in entities:
        # print(ent)
    asking_jeffrey = evalulate_next_input
    evalulated = False
    evalulate_next_input = False
    heard_jeffrey = False
    synonyms_list = []
    i = 0
    for word in docs:
        # print(word.text, word.pos_)
        syns = wordnet.synsets(word.text)
        # print(f'{word.text.upper()}')
        if not asking_jeffrey:
            if word.text in jeffrey:
                asking_jeffrey = True
                heard_jeffrey = True
            i += 1

        if asking_jeffrey:
            for syn in syns:
                # print(f'{syn.name()}: {syn.lemma_names()}')

                for lemma_sym in syn.lemma_names():
                    if not lemma_sym in synonyms_list:
                        synonyms_list.append(lemma_sym)

    if asking_jeffrey:
        highest_conf_skill = get_highest_confidence_skill(synonyms_list, docs[i:])
        if highest_conf_skill:
            highest_conf_skill.do(docs[i:])
            return

    if heard_jeffrey and not evalulated:
        evalulate_next_input = True
        print("Next sentence will be evaluated")


def get_highest_confidence_skill(synonyms_list, spoken_list):
    highest_conf = 0
    conf_skill = None
    for primary_trigger, skill in skills.registry.items():
        skill_conf = skill.get_confidence(synonyms_list, spoken_list)
        print(f'Confidence in {primary_trigger[0]}: {skill_conf}')
        if skill_conf > highest_conf:
            highest_conf = skill_conf
            conf_skill = skill
    return conf_skill