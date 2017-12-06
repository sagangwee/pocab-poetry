from Posey import reverseNgrams, setupModel, generateCouplet, poemProcessing
from nltk.corpus import gutenberg, wordnet as wn
import json
import string
import os
import random

def generate_n_gram(corpus):
    # In this example I'm using a corpus from NLTK - Gutenburg Project
    # Sara Bryant - Stories to Tell to Children
    sentences = gutenberg.sents(corpus)

    # Process text and collect reverse N-grams sentence by sentence
    # Do not do this word by word or you'll have incoherent N-grams that span sentences
    def processText(sentence):
        tokens = []
        for word in sentence:
            valid = True
            for c in word:
                if c in string.punctuation:
                    valid = False
            if valid:
                tokens.append(word.lower())
        return tokens
    ngrams = []
    for sentence in sentences:
        tokens = processText(sentence)
        ngrams += reverseNgrams(tokens, 3)

    # print string.punctuation
    model = setupModel(ngrams)

    with open(corpus+'.json', 'w') as outfile:
        json.dump(model, outfile)

def generate_synonym_title(title):
    synsets = wn.synsets(title)
    synonyms = []
    for synst in synsets:
        for word in synst.lemma_names():
            synonyms.append(word)
    if len(synonyms) == 0:
        return title.title()
    new_title = synonyms[random.randint(0, len(synonyms) - 1)]
    count = len(synonyms)
    while new_title == title and count > 0:
        new_title = synonyms[random.randint(0, len(synonyms) - 1)]
        count -=1
    return new_title.title()

def generate_poem(corpus_input):
    with open(corpus_input+'.json', 'r') as infile:
        corpus = json.load(infile)
    os.remove(corpus_input+'.json')
    # This will generate a couplet - AABB CCDD EEFF GGHH
    # With 8 lines, 10 words each line
    poem, title = generateCouplet(corpus, 8, 10)

    title = generate_synonym_title(title)

    # Handles capitilization and formatting
    poemProcessing(poem)


    return poem, title