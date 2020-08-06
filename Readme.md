# Django Udemy
https://www.udemy.com/course/programacao-web-com-django-framework-do-basico-ao-avancado/learn/lecture/15362316#overview


Instala pycharm CE
Cria novo projeto, nome django1 —> Ele já gera venv com o nome do projeto
Pip install Django
Pip freeze > requirements.txt


# Django - comandos
python manage.py runserver

python manage.py shell
>>> from core.models import Produto
>>> dir(Produto)  #verifica opcoes, tem objects, por exemplo

>>> dir(Produto.objects)

>>> produto = Produto.objects.all() # Retorna todos os objetos da classe Produto


Django-admin startproject django1 .
django-admin startapp core

#### Instala pacotes adicionais - módulo básico
pip install whitenoise gunicorn

<br>
O whitenoise é para servir arquivos estaticos durante producao, integrado com django
O Gunicorn é um servidor de aplicacao

<br>#### Heroku
Faz Login  
<br>⇒  heroku create django1-jw --buildpack heroku/python 
<br>⇒  git push heroku master 

