from django.urls import path
from .views import homepage, vendas

urlpatterns = [
    path('',homepage, name='homepage'),
    path('vendas/',vendas, name='vendas'),
    
]
