from django.urls import path
from .views import homepage, vendas, relatorios, estoque, caixa

app_name="sistema"

urlpatterns = [
    path('',homepage, name='homepage'),
    path('vendas/',vendas, name='vendas'),
    path('relatorios/',relatorios, name='relatorios'),
    path('estoque/',estoque, name='estoque'),
    path('caixa/',caixa, name='caixa'),
    
]
