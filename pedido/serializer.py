from rest_framework import serializers
from pedido.models import Pedido, Deliver
from prato.serializer import PratoSerializer
from prato.models import Prato


class PedidoSerializer(serializers.ModelSerializer):
    pratos = PratoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id', 'pratos', 'quantidade', 'mesa', 'observacao']


    def create_pratos(self, pratos, pedido):
        # criar o objeto prato
        for prato in pratos:
            pt = Prato.objects.create(**prato)
            pedido.pratos.add(pt)

    def create(self, validated_data):
        pratos = validated_data['pratos']
        del validated_data['pratos']
        pedido = Pedido.objects.create(**validated_data)
        self.create_pratos(pratos, pedido)

        return pedido

class DeliverSerializer(serializers.ModelSerializer):
    pratos = PratoSerializer(many=True)

    class Meta:
        model = Deliver
        fields = ['id', 'pratos', 'quantidade', 'local', 'observacao']

    def create_pratos(self, pratos, deliver):
        # criar o objeto prato
        for prato in pratos:
            pt = Prato.objects.create(**prato)
            deliver.pratos.add(pt)


    def create(self, validated_data):
        pratos = validated_data['pratos']
        del validated_data['pratos']
        deliver = Deliver.objects.create(**validated_data)
        self.create_pratos(pratos, deliver)

        return deliver