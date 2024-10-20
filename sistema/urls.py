from django.urls import path
from .views import homepage, Vendas, relatorios, Estoque, caixa, RelatorioDeVendas, RelatorioDeCaixa, cadastrarProduto, EditarProduto, clientes, fornecedores, entradaDeNotas, salvar_entrada

app_name="sistema"

urlpatterns = [
    path('',homepage, name='homepage'),
    path('vendas/',Vendas.as_view(), name='vendas'),
    path('relatorios/',relatorios, name='relatorios'),
    path('estoque/', Estoque.as_view(), name='estoque'),
    path('caixa/',caixa, name='caixa'),
    path('relatoriovendas/<int:pk>', RelatorioDeVendas.as_view(), name="relatorio_vendas"),
    path('relatoriocaixa/<int:pk>', RelatorioDeCaixa.as_view(), name="relatoriocaixa"),
    path('cadastrarproduto/', cadastrarProduto, name="cadastrarProduto"),
    path('editarproduto/<int:pk>', EditarProduto.as_view(), name="editarProduto"),
    path('clientes/', clientes, name="clientes"),
    path('fornecedores/', fornecedores, name="fornecedores"),
    path('entradaDeNotas', entradaDeNotas, name="entradaDeNotas"),
    path('salvar-entrada/', salvar_entrada, name='salvar_entrada'),
]
