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

def produto(request, pk):
    # Verifica se o parm pk está sendo recebido
    # print(f'PK: {pk}')

    prod = Produto.objects.get(id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)