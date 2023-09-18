from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from .models import RelatorioVendas, RelatorioCaixa, Produto
from django.contrib import messages
from django.urls import reverse

def homepage(request):
    return render(request, "homepage.html")


def vendas(request):
    return render(request, "vendas.html")

def relatorios(request):
    return render(request, "relatorios.html")


class Estoque(ListView):
    template_name = "estoque.html"
    model = Produto


def cadastrarProduto(request):
    if request.method == "POST":
        nome_produto = request.POST.get("nome-produto")
        grupo_produto = request.POST.get("grupo-produto")
        preco_custo = request.POST.get("preco-custo")
        preco_venda = request.POST.get("preco-venda")
        quantidade = request.POST.get("quantidade")
        try:
            preco_venda = preco_venda.replace(",",".")
            preco_custo = preco_custo.replace(",",".")
            preco_venda = float(preco_venda)
            preco_custo = float(preco_custo)
            quantidade = int(quantidade)
        except:
            messages.error(request, "Ocorreu um erro ao cadastrar o produto. Verifique os dados e tente novamente!")
            return render(request, "cadastrarProduto.html")
        Produto.objects.create(
            nome=nome_produto, valor_venda=preco_venda, valor_custo=preco_custo, quantidade=quantidade, grupo=grupo_produto
        )
        messages.success(request, "Produto cadastrado com sucesso!")

    
    return render(request, "cadastrarProduto.html")


def caixa(request):
    return render(request, "caixa.html")


class RelatorioDeVendas(DetailView):
    template_name = "relatorioVendas.html"
    model = RelatorioVendas



class RelatorioDeCaixa(DetailView):
    template_name = "relatorioCaixa.html"
    model = RelatorioCaixa


class EditarProduto(DetailView):
    template_name = "editarProduto.html"
    model = Produto

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            button_type = request.POST.get("confirm") 
            id = request.POST.get("id")
            if button_type == "edit":
                nome_produto = request.POST.get("nome-produto")
                grupo_produto = request.POST.get("grupo-produto")
                preco_custo = request.POST.get("preco-custo")
                preco_venda = request.POST.get("preco-venda")
                quantidade = request.POST.get("quantidade")
                try:
                    preco_venda = preco_venda.replace(",",".")
                    preco_custo = preco_custo.replace(",",".")
                    preco_venda = float(preco_venda)
                    preco_custo = float(preco_custo)
                    quantidade = int(quantidade)
                except:
                    messages.error(request, "Ocorreu um erro ao editar o produto. Verifique os dados e tente novamente!")
                    return redirect(reverse("sistema:editarProduto", args=[produto.id]))
                produto = get_object_or_404(Produto, id=id)
                produto.nome = nome_produto
                produto.grupo = grupo_produto
                produto.valor_custo = preco_custo
                produto.valor_venda = preco_venda
                produto.quantidade = quantidade
                produto.save()
                messages.success(request, "Produto editado com sucesso!")
                return redirect(reverse("sistema:editarProduto", args=[id]))
            if button_type == "del":
                try:
                    produto.get_object_or_404(Produto, id=id)
                    produto.delete()
                    messages.success(request, "Produto excluído com sucesso!")
                    return redirect("sistema:estoque")
                except:
                    messages.error(request, "Ocorreu um erro ao excluir o produto. Verifique os dados e tente novamente!")
                    return redirect(reverse("sistema:editarProduto", args=[id]))


