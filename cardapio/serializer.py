from rest_framework import serializers
from cardapio.models import Cardapio


class CardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardapio
        fields = ['id', 'nome', 'preco', 'descricao', 'quantidade']

