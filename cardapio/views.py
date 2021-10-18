from django.http import HttpResponse
from rest_framework import viewsets, generics, status
from rest_framework.decorators import action

from cardapio.models import Cardapio
from cardapio.serializer import CardapioSerializer
from rest_framework.response import Response
from prato.models import Prato
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class CardapioPratoViewset(viewsets.ModelViewSet):
    """Exibindo todos os pratos do cardapio"""
    serializer_class = CardapioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def get_queryset(self):
        cardapio = Cardapio.objects.all()
        return cardapio

    def create(self, request, *args, **kwargs):
        data = request.data

        new_cardapio = Cardapio.objects.create(nome=data["nome"], descricao=data["descricao"])

        new_cardapio.save()

        for prato in data["pratos"]:
            prato_obj = Prato.objects.get(nome=prato["nome"])
            new_cardapio.pratos.add(prato_obj)

        serializer = CardapioSerializer(new_cardapio)

        return Response(serializer.data)


# class CardapioCreate(generics.CreateAPIView):
#     serializer_class = CardapioSerializer
#     permission_classes = (IsAuthenticated,)
#     authentication_class = (TokenAuthentication,)
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         print(serializer)
#         print(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Cardapio criado'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


class CardapioList(viewsets.ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class CardapioDelete(viewsets.ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class CardapioUpdate(viewsets.ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def get_queryset(self):
        cardapio = Cardapio.objects.all()
        return cardapio

    def create(self, request, *args, **kwargs):
        data = request.data

        new_cardapio = Cardapio.objects.create(nome=data["nome"], descricao=data["descricao"])

        new_cardapio.save()

        for prato in data["pratos"]:
            prato_obj = Prato.objects.get(nome=prato["nome"])
            new_cardapio.pratos.add(prato_obj)

        serializer = CardapioSerializer(new_cardapio)

        return Response(serializer.data)

class CardapioDetail(viewsets.ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)




# class CreateCardapio(APIView):
#     def post(self, request):
#         get_dados = request.data
#         print(get_dados)
#         nome = get_dados['nome']
#         preco = get_dados['preco']
#         descricao = get_dados['descricao']
#         quantidade = get_dados['quantidade']
#
#         cliente = Cardapio.objects.create()
#         print('sddsf')
#         cliente.nome = nome
#         cliente.preco = preco
#         cliente.descricao = descricao
#         cliente.quantidade = quantidade
#         cliente.save()
#         return Response("Retorno", status=200)
