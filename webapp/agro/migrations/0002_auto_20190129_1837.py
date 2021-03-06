# Generated by Django 2.1.5 on 2019-01-29 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='endereco_complemento',
            field=models.CharField(max_length=100, null=True, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=20, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco_bairro',
            field=models.CharField(max_length=60, null=True, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco_celular',
            field=models.CharField(max_length=20, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco_cep',
            field=models.CharField(max_length=20, null=True, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco_cidade',
            field=models.CharField(max_length=60, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco_email',
            field=models.CharField(max_length=254, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco_email_confirmacao',
            field=models.CharField(max_length=254, null=True, verbose_name='Confirmação de e-mail'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco_estado',
            field=models.CharField(max_length=20, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco_logradouro',
            field=models.CharField(max_length=100, null=True, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco_numero',
            field=models.CharField(max_length=20, null=True, verbose_name='Numero'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='endereco_telefone',
            field=models.CharField(max_length=20, null=True, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome_completo',
            field=models.CharField(max_length=60, null=True, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rg',
            field=models.CharField(max_length=20, null=True, verbose_name='RG'),
        ),
    ]
