from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HTTP response
    return render(request, 'recipes/home.html') # Namespacing 

def sobre(request):
    return HttpResponse('SOBRE')                # DENTRO DA HILUX ELA MOVIMENTA NO HIT DO TUTS TUTS

def contato(request):
    return HttpResponse('CONTATO')