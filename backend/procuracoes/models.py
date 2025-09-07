from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Procuracao(models.Model):
    titular_name = models.CharField("Titular", max_length=200)
    procurador_name = models.CharField("Procurador", max_length=200, blank=True, null=True)
    description = models.TextField("Descrição", blank=True, null=True)
    issued_date = models.DateField("Data de Emissão")
    expiry_date = models.DateField("Data de Vencimento")
    priority = models.IntegerField("Prioridade", default=3)  # 1 alta .. 5 baixa
    status = models.CharField(
        "Status",
        max_length=20,
        choices=[("active", "Ativa"), ("expired", "Expirada"), ("renewed", "Renovada")],
        default="active",
    )
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def days_to_expiry(self):
        return (self.expiry_date - date.today()).days

    def __str__(self):
        return f"{self.titular_name} - expira em {self.expiry_date}"
