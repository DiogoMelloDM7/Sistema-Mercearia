from django.shortcuts import render

def homepage(request):
    return render(request, "homepage.html")


def vendas(request):
    return render(request, "vendas.html")

def relatorios(request):
    return render(request, "relatorios.html")

def estoque(request):
    return render(request, "estoque.html")

def caixa(request):
    return render(request, "caixa.html")
