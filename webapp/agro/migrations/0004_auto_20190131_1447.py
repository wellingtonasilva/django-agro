# Generated by Django 2.1.5 on 2019-01-31 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0003_ceplogradouro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ceplogradouro',
            name='complemento',
        ),
        migrations.RemoveField(
            model_name='ceplogradouro',
            name='numero',
        ),
    ]
