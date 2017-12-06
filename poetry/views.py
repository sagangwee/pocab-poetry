from django.shortcuts import render
from poem import generate_poem, generate_n_gram

def index(request):
    try:
        corpus = request.GET['corpus']
        if corpus == "":
        	corpus = 'shakespeare-macbeth.txt'
    except Exception as e:
        print e
        corpus = 'shakespeare-macbeth.txt'
    corpus_options = ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt',
        'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt',
        'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt',
        'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt',
        'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt',
        'shakespeare-macbeth.txt', 'whitman-leaves.txt']
    
    generate_n_gram(corpus)
    poem, title = generate_poem(corpus)
    
    context = {'poem': poem, 'title': title, 'corpus_options': corpus_options, 'corpus': corpus}
    return render(request, 'poetry/index.html', context)
