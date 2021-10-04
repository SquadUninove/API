from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from prato.models import Prato
from prato.serializer import PratoSerializer
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated







class PratoCreate(generics.CreateAPIView):
    serializer_class = PratoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Prato criado'}, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)



class PratoList(generics.ListAPIView):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class PratoDelete(generics.RetrieveDestroyAPIView):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class PratoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class PratoDetail(generics.RetrieveAPIView):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

