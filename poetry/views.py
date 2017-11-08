from django.shortcuts import render

def index(request):
	context = {'hello': 'world'}
	return render(request, 'poetry/index.html', context)
    
