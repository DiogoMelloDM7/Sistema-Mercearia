from django.urls import path
from .views import homepage, vendas, relatorios, Estoque, caixa, RelatorioDeVendas, RelatorioDeCaixa, cadastrarProduto, EditarProduto

app_name="sistema"

urlpatterns = [
    path('',homepage, name='homepage'),
    path('vendas/',vendas, name='vendas'),
    path('relatorios/',relatorios, name='relatorios'),
    path('estoque/', Estoque.as_view(), name='estoque'),
    path('caixa/',caixa, name='caixa'),
    path('relatoriovendas/<int:pk>', RelatorioDeVendas.as_view(), name="relatorio_vendas"),
    path('relatoriocaixa/<int:pk>', RelatorioDeCaixa.as_view(), name="relatoriocaixa"),
    path('cadastarproduto/', cadastrarProduto, name="cadastrarProduto"),
    path('editarproduto/<int:pk>', EditarProduto.as_view(), name="editarProduto"),
    
]
