from django.urls import include, path
from .views import CardapioCreate, CardapioDetail, CardapioList, CardapioUpdate, CardapioDelete



urlpatterns = [

    path('create/', CardapioCreate.as_view(), name='create-cardapio'),
    path('', CardapioList.as_view()),
    path('<int:pk>/', CardapioDetail.as_view(), name='retrieve-cardapio'),
    path('update/<int:pk>/', CardapioUpdate.as_view(), name='update-cardapio'),
    path('delete/<int:pk>/', CardapioDelete.as_view(), name='delete-cardapio')
]
