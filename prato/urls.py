from django.urls import include, path
from .views import PratoList, PratoDelete, PratoDetail, PratoUpdate, PratoCreate

urlpatterns = [
    path('create/', PratoCreate.as_view(), name='create-prato'),
    path('', PratoList.as_view()),
    path('<int:pk>/', PratoDetail.as_view(), name='retrieve-prato'),
    path('update/<int:pk>/', PratoUpdate.as_view(), name='update-prato'),
    path('delete/<int:pk>/', PratoDelete.as_view(), name='delete-prato')
]