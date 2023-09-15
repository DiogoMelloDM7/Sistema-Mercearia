from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import RelatorioVendas, RelatorioCaixa, Produto

def homepage(request):
    return render(request, "homepage.html")


def vendas(request):
    return render(request, "vendas.html")

def relatorios(request):
    return render(request, "relatorios.html")


class Estoque(ListView):
    template_name = "estoque.html"
    model = Produto


def caixa(request):
    return render(request, "caixa.html")


class RelatorioDeVendas(DetailView):
    template_name = "relatorioVendas.html"
    model = RelatorioVendas



class RelatorioDeCaixa(DetailView):
    template_name = "relatorioCaixa.html"
    model = RelatorioCaixa
