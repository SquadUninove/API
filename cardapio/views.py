from rest_framework import viewsets, generics
from cardapio.models import Cardapio
from cardapio.serializer import CardapioSerializer



class CardapioViewset(viewsets.ModelViewSet):
    """Exibindo todos os pratos do cardapio"""
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer



