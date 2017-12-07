from django.shortcuts import render
from scripts.poem import generate_poem, generate_n_gram
import random
def index(request):
    # generate_n_gram("trump
    trump_poem, trump_title = generate_poem("trump")
    # generate_n_gram("obama")
    obama_poem, obama_title = generate_poem("obama")
    poems = [(trump_poem, trump_title, "Trump"), (obama_poem, obama_title, "Obama")]

    choice = poems[random.choice([0,1])]

    poem, title, author  = choice
    data = {
      'poem': poem,
      'author': author,
      'title': title,
    }
    context = {
      'data': data
    }

    return render(request, 'poetry/index.html', context)
