from django.shortcuts import render
from django.http import HttpResponse
from .models import Metodo

# Create your views here.
def home(request):
    searchTerm = request.GET.get('searchMethod')
    if searchTerm:
        metodos = Metodo.objects.filter(title__icontains=searchTerm)
    else:
        metodos = Metodo.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'metodos': metodos})

def about(request):
    return HttpResponse('<h1>Welcome to the Jungle, baby (about)<h1>')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

