from django.shortcuts import render

def index(request):
    context = {
        'curso': 'Programacao Web com Django Framework',
        'outro': 'Djando eh massa!'
    }

    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

# Create your views here.
