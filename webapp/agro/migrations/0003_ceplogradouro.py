# Generated by Django 2.1.5 on 2019-01-31 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0002_auto_20190129_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='CepLogradouro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=20, null=True, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=100, null=True, verbose_name='Logradouro')),
                ('complemento', models.CharField(max_length=100, null=True, verbose_name='Complemento')),
                ('numero', models.CharField(max_length=20, null=True, verbose_name='Numero')),
                ('bairro', models.CharField(max_length=60, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=60, null=True, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=20, null=True, verbose_name='Estado')),
            ],
        ),
    ]