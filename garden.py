import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathsentences = ["The old man the boat", "The horse raced past the barn fell", "Mary gave the child a Band-Aid", "That Jill is never here hurts", "The cotton clothing is made of grows in mississippi" ]


for sentence in gardenpathsentences:
    doc = nlp(sentence)
    for ent in doc.ents:
        print(ent.text, ent.label_)