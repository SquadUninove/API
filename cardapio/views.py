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
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    @action(methods=['post'], detail=True)
    def associa_prato(self, request, pk):
        pratos = request.data['ids']
        cardapio = Cardapio.objects.get(id=pk)
        cardapio.pratos.set(pratos)
        cardapio.save()
        return HttpResponse('Pratos adicionados ao cardapio!')


class CardapioCreate(generics.CreateAPIView):
    serializer_class = CardapioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Cardapio criado'}, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


class CardapioList(generics.ListAPIView):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class CardapioDelete(generics.RetrieveDestroyAPIView):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class CardapioUpdate(generics.RetrieveUpdateAPIView):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class CardapioDetail(generics.RetrieveAPIView):
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
