from django import forms


class ClienteForm(forms.Form):
    id = forms.IntegerField(label='ID')
    cpf = forms.CharField(label='CPF', max_length=20)
    nome_completo = forms.CharField(label='Nome Completo', max_length=60)
    rg = forms.CharField(label='RG', max_length=20)
    endereco_cep = forms.CharField(label='CEP', max_length=20)
    endereco_logradouro = forms.CharField(label='Logradouro', max_length=100)
    endereco_complemento = forms.CharField(label='Complemento', max_length=100)
    endereco_numero = forms.CharField(label='Numero', max_length=20)
    endereco_bairro = forms.CharField(label='Bairro', max_length=60)
    endereco_cidade = forms.CharField(label='Cidade', max_length=60)
    endereco_estado = forms.CharField(label='Estado', max_length=20)
    endereco_celular = forms.CharField(label='Celular', max_length=20)
    endereco_telefone = forms.CharField(label='Telefone', max_length=20)
    endereco_email = forms.CharField(label='E-mail', max_length=254)
    endereco_email_confirmacao = forms.CharField(label='Confirmação de e-mail', max_length=254)

