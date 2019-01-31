from rest_framework import serializers
from .models import CepLogradouro


class CepLogradouroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CepLogradouro
        fields = ('cep', 'logradouro', 'bairro', 'cidade', 'estado')

