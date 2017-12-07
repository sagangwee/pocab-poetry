from django.shortcuts import render
from scripts.poem import generate_poem, generate_n_gram

def index(request):
    generate_n_gram("trump")
    trump_poem, trump_title = generate_poem("trump")
    generate_n_gram("obama")
    obama_poem, obama_title = generate_poem("obama")

    context = {
      'obama_poem': obama_poem,
      'obama_title': obama_title,
      'trump_poem': trump_poem,
      'trump_title': trump_title
    }

    return render(request, 'poetry/index.html', context)
