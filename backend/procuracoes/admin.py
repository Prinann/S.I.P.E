from django.contrib import admin
from .models import Procuracao

@admin.register(Procuracao)
class ProcuracaoAdmin(admin.ModelAdmin):
    list_display = ("titular_name", "procurador_name", "expiry_date", "priority", "status", "days_to_expiry")
    list_filter = ("status", "priority")
    search_fields = ("titular_name", "procurador_name")
