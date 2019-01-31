from django.contrib import admin
from .models import Cliente, CepLogradouro


# Register your models here.
@admin.register(Cliente)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome_completo')
    list_filter = ['cpf', 'nome_completo']
    search_fields = ['cpf', 'nome_completo']


@admin.register(CepLogradouro)
class CepLogradouroAdmin(admin.ModelAdmin):
    list_display = ('cep', 'logradouro', 'bairro', 'cidade', 'estado')
    list_filter = ['cep', 'logradouro', 'bairro', 'cidade', 'estado']
    search_fields = ['cep', 'logradouro', 'bairro', 'cidade', 'estado']
