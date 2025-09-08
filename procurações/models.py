from django.db import models
from django.utils import timezone

class Procuracao(models.Model):
    nome_cliente = models.CharField(max_length=200)
    numero_procuracao = models.CharField(max_length=50, unique=True)
    data_emissao = models.DateField(default=timezone.now)
    data_vencimento = models.DateField()
    prioridade = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.nome_cliente} - {self.numero_procuracao}"
