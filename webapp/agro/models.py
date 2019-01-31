from django.db import models


# Create your models here.
class Cliente(models.Model):
    cpf = models.CharField('CPF', max_length=20, null=True)
    nome_completo = models.CharField('Nome Completo', max_length=60, null=True)
    rg = models.CharField('RG', max_length=20, null=True)
    endereco_cep = models.CharField('CEP', max_length=20, null=True)
    endereco_logradouro = models.CharField('Logradouro', max_length=100, null=True)
    endereco_complemento = models.CharField('Complemento', max_length=100, null=True)
    endereco_numero = models.CharField('Numero', max_length=20, null=True)
    endereco_bairro = models.CharField('Bairro', max_length=60, null=True)
    endereco_cidade = models.CharField('Cidade', max_length=60, null=True)
    endereco_estado = models.CharField('Estado', max_length=20, null=True)
    endereco_celular = models.CharField('Celular', max_length=20, null=True)
    endereco_telefone = models.CharField('Telefone', max_length=20, null=True)
    endereco_email = models.CharField('E-mail', max_length=254, null=True)
    endereco_email_confirmacao = models.CharField('Confirmação de e-mail', max_length=254, null=True)

    def __str__(self):
        return self.nome_completo


class CepLogradouro(models.Model):
    cep = models.CharField('CEP', max_length=20, null=True)
    logradouro = models.CharField('Logradouro', max_length=100, null=True)
    bairro = models.CharField('Bairro', max_length=60, null=True)
    cidade = models.CharField('Cidade', max_length=60, null=True)
    estado = models.CharField('Estado', max_length=20, null=True)

