from rest_framework import serializers
from cardapio.models import Cardapio
from prato.serializer import PratoSerializer
from prato.models import Prato

class CardapioSerializer(serializers.ModelSerializer):
    pratos = PratoSerializer(many=True)

    class Meta:
        model = Cardapio
        fields = ['id', 'nome', 'pratos', 'descricao']

    def create_pratos(self, pratos, cardapio):
        # criar o objeto prato
        for prato in pratos:
            pt = Prato.objects.create(**prato)
            cardapio.pratos.add(pt)


    def create(self, validated_data):
        pratos = validated_data['pratos']
        del validated_data['pratos']
        cardapio = Cardapio.objects.create(**validated_data)
        self.create_pratos(pratos, cardapio)

        return cardapio





