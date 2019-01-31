from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente, CepLogradouro
from .forms import ClienteForm
from .serializers import CepLogradouroSerializer


def login_page(request):
    return render(request, 'login.html', {'servers': ''})


def principal(request):
    return render(request, 'index.html', {})


@login_required(login_url='/agro')
def listagem(request):
    list_cliente = []
    page = request.GET.get('page')
    if page is None:
        page = 1
    if request.method == 'POST':
        listagem_search = request.POST['listagem_search']
        try:
            list_cliente = Cliente.objects.filter(
                Q(cpf__contains=listagem_search) | Q(nome_completo__contains=listagem_search)
            )
        except Cliente.DoesNotExist:
            pass
    else:
        list_cliente = Cliente.objects.order_by('cpf')
    paginator = Paginator(list_cliente, 5)
    clientes = paginator.get_page(page)
    return render(request, 'listagem.html', {'list_cliente': clientes, 'num_page': page})


@login_required(login_url='/agro')
def cliente_novo(request):
    form = ClienteForm({'id': -1})
    return render(request, 'cliente_novo.html', {'cliente': form})


@login_required(login_url='/agro')
def cliente_add(request):
    form = ClienteForm(request.POST)
    if form.is_valid():
        cliente = Cliente()
        cliente.cpf = form.cleaned_data['cpf']
        cliente.nome_completo = form.cleaned_data['nome_completo']
        cliente.rg = form.cleaned_data['rg']
        cliente.endereco_cep = form.cleaned_data['endereco_cep']
        cliente.endereco_logradouro = form.cleaned_data['endereco_logradouro']
        cliente.endereco_complemento = form.cleaned_data['endereco_complemento']
        cliente.endereco_numero = form.cleaned_data['endereco_numero']
        cliente.endereco_bairro = form.cleaned_data['endereco_bairro']
        cliente.endereco_cidade = form.cleaned_data['endereco_cidade']
        cliente.endereco_estado = form.cleaned_data['endereco_estado']
        cliente.endereco_celular = form.cleaned_data['endereco_celular']
        cliente.endereco_telefone = form.cleaned_data['endereco_telefone']
        cliente.endereco_email = form.cleaned_data['endereco_email']
        cliente.endereco_email_confirmacao = form.cleaned_data['endereco_email_confirmacao']
        cliente.save()
        return HttpResponseRedirect('/agro/listagem')
    else:
        return render(request, 'cliente_novo.html', {'cliente': form})


@login_required(login_url='/agro')
def cliente_save(request, id):
    form = ClienteForm(request.POST)
    if form.is_valid():
        cliente = Cliente.objects.get(pk=id)
        cliente.cpf = form.cleaned_data['cpf']
        cliente.nome_completo = form.cleaned_data['nome_completo']
        cliente.rg = form.cleaned_data['rg']
        cliente.endereco_cep = form.cleaned_data['endereco_cep']
        cliente.endereco_logradouro = form.cleaned_data['endereco_logradouro']
        cliente.endereco_complemento = form.cleaned_data['endereco_complemento']
        cliente.endereco_numero = form.cleaned_data['endereco_numero']
        cliente.endereco_bairro = form.cleaned_data['endereco_bairro']
        cliente.endereco_cidade = form.cleaned_data['endereco_cidade']
        cliente.endereco_estado = form.cleaned_data['endereco_estado']
        cliente.endereco_celular = form.cleaned_data['endereco_celular']
        cliente.endereco_telefone = form.cleaned_data['endereco_telefone']
        cliente.endereco_email = form.cleaned_data['endereco_email']
        cliente.endereco_email_confirmacao = form.cleaned_data['endereco_email_confirmacao']
        cliente.save()
        return HttpResponseRedirect('/agro/listagem')
    else:
        return render(request, 'cliente_edit.html', {'cliente': form})


@login_required(login_url='/agro')
def cliente_edit(request, id):
    cliente = Cliente.objects.get(pk=id)
    return render(request, 'cliente_edit.html', {'cliente': cliente})


@login_required(login_url='/agro')
def cliente_delete(request, id):
    cliente = Cliente.objects.get(pk=id)
    cliente.delete()
    return HttpResponseRedirect('/agro/listagem')


@login_required(login_url='/agro')
def cliente_view(request, id):
    cliente = Cliente.objects.get(pk=id)
    return render(request, 'cliente_view.html', {'cliente': cliente})


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def check_login(request):
    username = request.POST['login_username']
    password = request.POST['login_password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/agro/listagem')
    else:
        return render(request, 'login.html', {})


@api_view(['GET', 'POST'])
def get_endereco(request):
    try:
        cep_logradouro = CepLogradouro.objects.get(cep=request.GET['endereco_cep'])
    except CepLogradouro.DoesNoExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CepLogradouroSerializer(cep_logradouro, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

