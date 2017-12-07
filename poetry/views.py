from django.shortcuts import render
from scripts.poem import generate_poem, generate_n_gram
import random
from .forms import VoteForm
def index(request):
    # generate_n_gram("trump")
    vote = None
    data = None
    if request.method=="GET":
      form = VoteForm(request.GET)
      if form.is_valid():
        vote = form.cleaned_data['vote']
        data = form.cleaned_data['data']
    trump_poem, trump_title = generate_poem("trump")
    # generate_n_gram("obama")
    obama_poem, obama_title = generate_poem("obama")
    poems = [(trump_poem, trump_title, "Trump"), (obama_poem, obama_title, "Obama")]
    
    choice = poems[random.choice([0,1])]
    
    poem, title, author  = choice
    if not data:
      data = {
        'poem': poem,
        'author': author,
        'title': title,
      }
    context = {
      'data': data
    }

    return render(request, 'poetry/index.html', context)
