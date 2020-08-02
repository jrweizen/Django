from django.contrib import admin

from .models import Produto, Cliente

# Exibicao do Produto - utilizar snake case
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

# Exibicao do Cliente
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

# Registrando
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)


