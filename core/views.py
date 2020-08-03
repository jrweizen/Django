from django.shortcuts import render
from .models import Produto

def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso': 'Programacao Web com Django Framework',
        'outro': 'Djando eh massa!',
        'produtos': produtos
    }

    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

# Create your views here.
