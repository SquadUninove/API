from django.urls import include, path
from rest_framework import routers

from .views import PedidoCreate, PedidoDetail, PedidoList, PedidoUpdate, PedidoDelete, PedidoViewset




urlpatterns = [

    path('create/', PedidoCreate.as_view(), name='create-pedido'),
    path('', PedidoList.as_view()),
    path('<int:pk>/', PedidoDetail.as_view(), name='retrieve-pedido'),
    path('update/<int:pk>/', PedidoUpdate.as_view(), name='update-pedido'),
    path('delete/<int:pk>/', PedidoDelete.as_view(), name='delete-pedido')
]
