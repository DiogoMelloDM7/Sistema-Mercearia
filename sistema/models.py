from django.db import models
from django.utils import timezone

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    grupo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    produtos = models.ManyToManyField(Produto, through="ItensVenda")
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(default=timezone.now)
    

class ItensVenda(models.Model):
    venda = models.ForeignKey("Venda", related_name="venda", on_delete=models.CASCADE)
    produto = models.ForeignKey("Produto", related_name="produtos_do_item", on_delete=models.CASCADE)
    quantidade = models.IntegerField()


class RelatorioVendas(models.Model):
    vendas = models.ForeignKey("Venda", related_name="vendas_relatorio", on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now)


class RelatorioCaixa(models.Model):
    valorSistema = models.DecimalField(max_digits=10, decimal_places=2) 
    valorCaixa = models.DecimalField(max_digits=10, decimal_places=2) 
    saldoFinal = models.DecimalField(max_digits=10, decimal_places=2) 
    data = models.DateTimeField(default=timezone.now)

