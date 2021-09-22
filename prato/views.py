from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from prato.models import Prato
from prato.serializer import PratoSerializer







class PratoCreate(generics.CreateAPIView):
    serializer_class = PratoSerializer

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

class PratoDelete(generics.RetrieveDestroyAPIView):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer

class PratoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer

class PratoDetail(generics.RetrieveAPIView):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer

