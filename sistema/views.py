from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from .models import RelatorioVendas, RelatorioCaixa, Produto, Credito, Debito
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from datetime import date
from decimal import Decimal


def homepage(request):
    return render(request, "homepage.html")


lista_vendas = []
class Vendas(ListView):
    template_name = "vendas.html"
    model = Produto

    def post(self, request, *args, **kwargs):
        button_type = request.POST.get("confirm")
        valor_total_venda = 0
        if button_type == "search":
            termo_busca = request.POST.get("busca-produto","")
            if termo_busca:
                produtos = Produto.objects.filter(Q(nome__icontains=termo_busca) | Q(grupo__icontains=termo_busca))
            else:
                produtos = Produto.objects.all()
            return render(request, self.template_name, {"object_list":produtos, "itens_venda": lista_vendas, "valor_total_venda": valor_total_venda})
        if button_type == "add":
            id_produto = request.POST.get("produto")
            quantidade = request.POST.get("quantidade")
            valor = request.POST.get("valor")
            produto = Produto.objects.filter(pk=id_produto).first()
            #try:
            if valor:
                quantidade = int(quantidade)
                valor = valor.replace(",",".")
                valor = float(valor)
            else:
                valor = 0
            #except:
                #messages.error(request, "Ocorreu um erro ao processar os dados inseridos, verifique os dados e #tente novamente!")
                #return render(request, self.template_name)
            valor_total = quantidade * valor
            
            itens_do_pedido = (produto.nome, quantidade, valor, valor_total)
            lista_vendas.append(itens_do_pedido)
            for item in lista_vendas:
                valor_total_venda += item[3]
            return render(request, self.template_name, {"itens_venda":lista_vendas, "valor_total_venda": valor_total_venda})


        
        


def relatorios(request):
    return render(request, "relatorios.html")


class Estoque(ListView):
    template_name = "estoque.html"
    model = Produto

    def post(self, request, *args, **kwargs):
        termo_busca = request.POST.get("busca-produto","")
        if termo_busca:
            produtos = Produto.objects.filter(Q(nome__icontains=termo_busca) | Q(grupo__icontains=termo_busca))
        else:
            produtos = Produto.objects.all()
        
        return render(request, self.template_name, {"object_list":produtos})


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
    if request.method == "POST":
        button_type = request.POST.get("confirm")
        if button_type == "calcula-valor":
            cent5 = float(request.POST.get("5-cent", 0))  # O segundo argumento (0) é um valor padrão caso o campo esteja vazio
            cent10 = float(request.POST.get("10-cent", 0))
            cent25 = float(request.POST.get("25-cent", 0))
            cent50 = float(request.POST.get("50-cent", 0))
            real1 = float(request.POST.get("1-real", 0))
            real2 = float(request.POST.get("2-real", 0))
            real5 = float(request.POST.get("5-real", 0))
            real10 = float(request.POST.get("10-real", 0))
            real20 = float(request.POST.get("20-real", 0))
            real50 = float(request.POST.get("50-real", 0))
            real100 = float(request.POST.get("100-real", 0))

            cent5 = cent5 * 0.05
            cent10 = cent10 * 0.1
            cent25 = cent25 * 0.25
            cent50 = cent50 * 0.5
            real1 = real1 * 1
            real2 = real2 * 2
            real5 = real5 * 5
            real10 = real10 * 10
            real20 = real20 * 25
            real50 = real50 * 50
            real100 = real100 * 100
            total = cent5 + cent10 + cent25 + cent50 + real1 + real2 + real5 + real10 + real20 + real50 + real100
            total = Decimal(total)
            data_hoje = date.today()
            relatorio = RelatorioCaixa.objects.filter(data__date=data_hoje).first()
            if not relatorio:
                RelatorioCaixa.objects.create(valorCaixa=total, valorSistema=0, saldoFinal=0)
            else:
                relatorio.valorCaixa = total
                relatorio.saldoFinal = relatorio.valorCaixa - relatorio.valorSistema
                relatorio.save()

            return render(request, "caixa.html", {"cent5": cent5, "cent10": cent10, "cent25": cent25, "cent50": cent50, "real1": real1, "real2": real2, "real5": real5, "real10": real10, "real20": real20, "real50": real50, "real100": real100, "total":total, "relatorio": relatorio})
        
        if button_type == "confirm-exit":
            descricao = request.POST.get("descricao-saida")
            valor = request.POST.get("valor-saida")
            data_hoje = date.today()
            relatorio = RelatorioCaixa.objects.filter(data__date=data_hoje).first()
            if not relatorio:
                valor = Decimal(valor)
                relatorio = RelatorioCaixa.objects.create(valorSistema=(-valor), saldoFinal=0, saldoCaixa=0)
                Credito.objects.create(descricao=descricao, valor=valor, relatorio_caixa=relatorio)
            else:
                valor = Decimal(valor)
                relatorio.valorSistema -= valor
                relatorio.saldoFinal = relatorio.valorCaixa - relatorio.valorSistema
                relatorio.save()
                Debito.objects.create(descricao=descricao, valor=valor, relatorio_caixa=relatorio)
            return render(request, "caixa.html", {"relatorio":relatorio})

        if button_type == "confirm-deposit":
            descricao = request.POST.get("descricao-entrada")
            valor = request.POST.get("valor-entrada")
            data_hoje = date.today()
            relatorio = RelatorioCaixa.objects.filter(data__date=data_hoje).first()
            if not relatorio:
                valor = Decimal(valor)
                relatorio = RelatorioCaixa.objects.create(valorSistema=(valor), saldoFinal=0, saldoCaixa=0)
                Credito.objects.create(descricao=descricao, valor=valor, relatorio_caixa=relatorio)
                
            else:
                valor = Decimal(valor)
                relatorio.valorSistema += valor
                relatorio.saldoFinal = relatorio.valorCaixa - relatorio.valorSistema
                relatorio.save()
                Credito.objects.create(descricao=descricao, valor=valor, relatorio_caixa=relatorio)
            return render(request, "caixa.html", {"relatorio":relatorio})

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
                    produto = get_object_or_404(Produto, id=id)
                    produto.delete()
                    messages.success(request, "Produto excluído com sucesso!")
                    return redirect("sistema:estoque")
                except:
                    messages.error(request, "Ocorreu um erro ao excluir o produto. Verifique os dados e tente novamente!")
                    return redirect(reverse("sistema:editarProduto", args=[id]))


