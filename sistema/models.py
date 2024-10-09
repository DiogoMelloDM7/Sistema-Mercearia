from django.db import models
from django.utils import timezone

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    valor_custo = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    grupo = models.CharField(max_length=100)
    quantidade_minima_para_pedido = models.IntegerField()

    def __str__(self):
        return self.nome + " - " + self.grupo


class Venda(models.Model):
    cliente = models.ForeignKey("Cliente", related_name="vendas", on_delete=models.CASCADE)
    relatorio = models.ForeignKey("RelatorioVendas", related_name="vendas", on_delete=models.CASCADE, blank=True, null=True)
    produtos = models.ManyToManyField(Produto, through="ItensVenda")
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Venda {self.pk} - Cliente"
    

class ItensVenda(models.Model):
    venda = models.ForeignKey("Venda", related_name="venda", on_delete=models.CASCADE)
    produto = models.ForeignKey("Produto", related_name="produtos_do_item", on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.produto.nome + " - " + f"Venda {self.venda.pk}"


class RelatorioVendas(models.Model):
    data = models.DateTimeField(default=timezone.now)
    valorfinal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.data}"




class RelatorioCaixa(models.Model):
    valorSistema = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    valorCaixa = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    valorCartao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    saldoFinal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.data}"


class Credito(models.Model):
    relatorio_caixa = models.ForeignKey("RelatorioCaixa", related_name="credito", on_delete=models.CASCADE, null=True, blank=True)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self): 
        return self.descricao


class Debito(models.Model):
    relatorio_caixa = models.ForeignKey("RelatorioCaixa", related_name="debito", on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self): 
        return self.descricao


class Cartao(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2) 
    venda = models.ForeignKey("Venda", related_name='cartao', on_delete=models.CASCADE)

    def __str__(self):
        return "Cartão de R$ " + f"{self.valor}" + " referente a venda de ID " + f"{self.venda}"
    

class Cliente(models.Model):
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    rua = models.CharField(max_length=100, null=False, blank=False)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return self.nome
    