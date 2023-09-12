from django.contrib import admin
from .models import Venda, Produto, RelatorioCaixa, RelatorioVendas, ItensVenda

# Register your models here.

admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(RelatorioCaixa)
admin.site.register(RelatorioVendas)
admin.site.register(ItensVenda)
