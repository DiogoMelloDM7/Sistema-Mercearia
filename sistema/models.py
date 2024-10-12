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
        return f"Venda {self.pk} - {self.cliente.nome}"
    

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
    cpf = models.CharField(max_length=100, null=False, blank=False, unique=True)
    telefone = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return self.nome
    
from django.db import models

class Fornecedor(models.Model):
    nome_empresa = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    inscricao_estadual = models.CharField(max_length=20, null=True, blank=True, default="")
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=30)
    cep = models.CharField(max_length=9)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_empresa

class NotaDeMercadoria(models.Model):
    numero_nota = models.CharField(max_length=50) 
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Valor total da nota
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='notas')
    data = models.DateTimeField(default=timezone.now)
    produtos = models.ManyToManyField(Produto, through='ItensNota')

    def __str__(self):
        return f"Nota {self.numero_nota} - {self.fornecedor.nome_empresa}"

class ItensNota(models.Model):
    nota = models.ForeignKey(NotaDeMercadoria, related_name="itens", on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name="produtos_da_nota", on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.quantidade} de {self.produto.nome} - Nota {self.nota.numero_nota}"
