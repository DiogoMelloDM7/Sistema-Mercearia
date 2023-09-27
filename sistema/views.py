from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from .models import RelatorioVendas, RelatorioCaixa, Produto, Credito, Debito, Venda, ItensVenda, Cartao
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q, Sum
from datetime import date, datetime
from decimal import Decimal, ROUND_DOWN


def homepage(request):
    return render(request, "homepage.html")


def limpa_lista_vendas():
    global lista_vendas
    lista_vendas = []

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
            try:
                if valor:
                    quantidade = int(quantidade)
                    valor = valor.replace(",",".")
                    valor = float(valor)
            
            except:
                messages.error(request, "Ocorreu um erro ao processar os dados inseridos, verifique os dados e tente novamente!")
                return render(request, self.template_name, {"itens_venda":lista_vendas, "valor_total_venda": valor_total_venda})
            valor_total = quantidade * valor
            
            itens_do_pedido = (produto.nome, quantidade, valor, valor_total)
            lista_vendas.append(itens_do_pedido)
            for item in lista_vendas:
                valor_total_venda += item[3]
            return render(request, self.template_name, {"itens_venda":lista_vendas, "valor_total_venda": valor_total_venda})
        if button_type == "del":
            indice = request.POST.get("indice")
            try: 
                indice = int(indice)
                indice -= 1
            except:
                indice = None
            try:
                if indice:
                    lista_vendas.pop(indice)
                else:
                    lista_vendas.pop(0)
                for item in lista_vendas:
                    valor_total_venda += item[3]
                
                return render(request, self.template_name, {"itens_venda": lista_vendas, "valor_total_venda": valor_total_venda})
            except: 
                return render(request, self.template_name, {"itens_venda": lista_vendas, "valor_total_venda": valor_total_venda})
        if button_type == "confirm-sale":
            if lista_vendas:
                data_hoje = date.today()
                relatorio_venda = RelatorioVendas.objects.filter(data__date=data_hoje).first()
                if not relatorio_venda:
                    relatorio_venda = RelatorioVendas.objects.create(valorfinal = 0)
                venda = Venda.objects.create(relatorio = relatorio_venda, valor = 0)
                
                for item in lista_vendas:
                    nome_produto = item[0]
                    quantidade = item[1]
                    valor_total_venda += item[3]
                    produto = Produto.objects.filter(nome=nome_produto).first()
                    produto.quantidade -= quantidade
                    if produto.quantidade < 0:
                        messages.error(request, f"O item {nome_produto} não possui estoque suficiente para completar essa venda!")
                        return render(request, self.template_name, {"itens_venda": lista_vendas, "valor_total_venda": valor_total_venda})
                    produto.save()
                    ItensVenda.objects.create(venda=venda, produto = produto, quantidade = quantidade)
                venda.valor = Decimal(valor_total_venda)
                venda.save()
                forma_pagamento = request.POST.get("pagamento")
                data_hoje = date.today()
                relatorio = RelatorioCaixa.objects.filter(data__date=data_hoje).first()
                if not relatorio:
                    relatorio = RelatorioCaixa.objects.create(valorCaixa=0, valorSistema=Decimal(valor_total_venda), saldoFinal=0, valorCartao=0)
                else:
                    relatorio.valorSistema += Decimal(valor_total_venda)
                    relatorio.save()
                if forma_pagamento == "cartao":
                    relatorio.valorCartao += Decimal(valor_total_venda)
                    relatorio.save()
                    Cartao.objects.create(valor=Decimal(valor_total_venda), venda=venda)
                limpa_lista_vendas()
                if forma_pagamento == "dinheiro+cartao":
                    try:
                        valor_dinheiro = request.POST.get('valor-dinheiro')
                        valor_cartao = request.POST.get('valor-cartao')
                        valor_dinheiro = valor_dinheiro.replace(",",".")
                        valor_cartao = valor_cartao.replace(",",".")
                        valor_cartao = Decimal(valor_cartao)
                        valor_dinheiro = Decimal(valor_dinheiro)
                        valor_total_venda = Decimal(valor_total_venda)
                        decimal_context = Decimal('0.01')
                        # Quantize os valores com duas casas decimais
                        valor_total_venda = valor_total_venda.quantize(decimal_context, rounding=ROUND_DOWN)
                        valor_cartao = valor_cartao.quantize(decimal_context, rounding=ROUND_DOWN)
                        valor_dinheiro = valor_dinheiro.quantize(decimal_context, rounding=ROUND_DOWN)
                        if (valor_cartao + valor_dinheiro) != valor_total_venda:
                            messages.error(request, "Valor inserido não bate com o valor da compra, verifique os dados e tente novamente!")
                            return render(request, self.template_name, {"itens_venda": lista_vendas, "valor_total_venda": valor_total_venda})
                        relatorio.valorCartao += valor_cartao
                        relatorio.save()
                        Cartao.objects.create(valor=Decimal(valor_cartao), venda=venda)
                        relatorio_venda.valorfinal += Decimal(valor_cartao)
                    except:
                        messages.error(request, "Verifique os dados inseridos e tente novamente, use apenas numeros e ponto ou virgula! Exemplo 15,99 ou 7.99!")
                relatorio_venda.valorfinal += Decimal(valor_total_venda)
                relatorio_venda.save()
                return render(request, self.template_name, {"itens_venda": lista_vendas, "valor_total_venda": valor_total_venda})
            else:
                messages.error(request, "Para finalizar uma venda, você precisa inserir algum item!")
                return render(request, self.template_name, {"itens_venda": lista_vendas, "valor_total_venda": valor_total_venda})



        
        


def relatorios(request):
    lista_relatorios_caixa = []
    lista_relatorios_venda = []
    if request.method == "POST":
        tipo_relatorio = request.POST.get('relatorio')
        data_inicial = request.POST.get("datainicio")
        data_final = request.POST.get("datafinal")

        # Converta as datas em objetos de data do Python
        data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d").date()
        data_final = datetime.strptime(data_final, "%Y-%m-%d").date()

        if tipo_relatorio == "relatorio-caixa":
            # Consulta para relatório de caixa entre datas
            relatorios_caixa = RelatorioCaixa.objects.filter(data__date__range=(data_inicial, data_final))
            lista_relatorios_caixa = [(relatorio.data.date(), relatorio.valorSistema, relatorio.valorCaixa, relatorio.pk) for relatorio in relatorios_caixa]

        elif tipo_relatorio == "relatorio-vendas":
            # Consulta para relatório de vendas entre datas
            relatorios_vendas = RelatorioVendas.objects.filter(data__date__range=(data_inicial, data_final))
            lista_relatorios_venda = [(relatorio.data.date(), relatorio.valorfinal, relatorio.pk) for relatorio in relatorios_vendas]

    return render(request, "relatorios.html", {"lista_relatorios_venda": lista_relatorios_venda, "lista_relatorios_caixa": lista_relatorios_caixa})



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
                relatorio.saldoFinal = (relatorio.valorCaixa + relatorio.valorCartao) - relatorio.valorSistema
                relatorio.save()

            return render(request, "caixa.html", {"cent5": cent5, "cent10": cent10, "cent25": cent25, "cent50": cent50, "real1": real1, "real2": real2, "real5": real5, "real10": real10, "real20": real20, "real50": real50, "real100": real100, "total":total, "relatorio": relatorio})
        
        if button_type == "confirm-exit":
            descricao = request.POST.get("descricao-saida")
            valor = request.POST.get("valor-saida")
            data_hoje = date.today()
            relatorio = RelatorioCaixa.objects.filter(data__date=data_hoje).first()
            try:
                if not relatorio:
                    valor = valor.replace(",",".")
                    valor = Decimal(valor)
                    relatorio = RelatorioCaixa.objects.create(valorSistema=(-valor), saldoFinal=0, saldoCaixa=0)
                    Credito.objects.create(descricao=descricao, valor=valor, relatorio_caixa=relatorio)
                else:
                    valor = valor.replace(",",".")
                    valor = Decimal(valor)
                    relatorio.valorSistema -= valor
                    relatorio.saldoFinal = (relatorio.valorCaixa + relatorio.valorCartao) - relatorio.valorSistema
                    relatorio.save()
                    Debito.objects.create(descricao=descricao, valor=valor, relatorio_caixa=relatorio)
            except:
                messages.error(request, "Ocorreu um erro ao debitar o valor, verifique os dados inseridos e tente novamente por favor!")
            return render(request, "caixa.html", {"relatorio":relatorio})

        if button_type == "confirm-deposit":
            descricao = request.POST.get("descricao-entrada")
            valor = request.POST.get("valor-entrada")
            data_hoje = date.today()
            relatorio = RelatorioCaixa.objects.filter(data__date=data_hoje).first()
            try:
                if not relatorio:
                    valor = valor.replace(",",".")
                    valor = Decimal(valor)
                    relatorio = RelatorioCaixa.objects.create(valorSistema=(valor), saldoFinal=0, saldoCaixa=0)
                    Credito.objects.create(descricao=descricao, valor=valor, relatorio_caixa=relatorio)
                    
                else:
                    valor = valor.replace(",",".")
                    valor = Decimal(valor)
                    relatorio.valorSistema += valor
                    relatorio.saldoFinal = (relatorio.valorCaixa + relatorio.valorCartao) - relatorio.valorSistema
                    relatorio.save()
                    Credito.objects.create(descricao=descricao, valor=valor, relatorio_caixa=relatorio)
            except:
                messages.error(request, "Ocorreu um erro ao creditar o valor, verifique os dados inseridos e tente novamente por favor!")
            return render(request, "caixa.html", {"relatorio":relatorio})

    return render(request, "caixa.html")



class RelatorioDeVendas(DetailView):
    template_name = "relatorioVendas.html"
    model = RelatorioVendas



class RelatorioDeCaixa(DetailView):
    template_name = "relatorioCaixa.html"
    model = RelatorioCaixa

    def get_context_data(self, **kwargs):
       try:
            context = super().get_context_data(**kwargs)
            relatorio = self.get_object()
            date = relatorio.data.date()
            relatorio_venda = get_object_or_404(RelatorioVendas, data__date=date)
            valor_total_vendas = relatorio_venda.valorfinal
            context['valor_total_vendas'] = valor_total_vendas
           
            valorcredito = relatorio.credito.aggregate(Sum('valor'))['valor__sum'] or 0
            valordebito = relatorio.debito.aggregate(Sum('valor'))['valor__sum'] or 0

            valor_total = (valor_total_vendas + valorcredito) - valordebito
            context['valor_total'] = valor_total

            return context
       except:
           messages.error(self.request, "Ocorreu um erro ao carregar o relatório, parece que algumas informações foram corrompidas!")
           return
            


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


