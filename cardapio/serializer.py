from rest_framework import serializers
from cardapio.models import Cardapio
from prato.serializer import PratoSerializer
from prato.models import Prato

class CardapioSerializer(serializers.ModelSerializer):
    pratos = PratoSerializer(many=True)

    class Meta:
        model = Cardapio
        fields = ['id', 'nome', 'pratos', 'descricao']










