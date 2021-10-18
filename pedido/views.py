from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from prato.models import Prato
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from pedido.serializer import PedidoSerializer
from pedido.models import Pedido



class PedidoViewset(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def get_queryset(self):
        pedido = Pedido.objects.all()
        return pedido

    def create(self, request, *args, **kwargs):
        data = request.data

        new_pedido = Pedido.objects.create(quantidade=data["quantidade"], mesa=data["mesa"], observacao=data["observacao"])

        new_pedido.save()

        for prato in data["pratos"]:
            prato_obj = Prato.objects.get(nome=prato["nome"])
            new_pedido.pratos.add(prato_obj)

        serializer = PedidoSerializer(new_pedido)

        return Response(serializer.data)


class PedidoCreate(generics.CreateAPIView):
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Pedido realizado'}, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


class PedidoList(generics.ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class PedidoDelete(generics.RetrieveDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class PedidoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class PedidoDetail(generics.RetrieveAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


