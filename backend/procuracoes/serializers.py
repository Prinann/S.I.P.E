from rest_framework import serializers
from .models import Procuracao

class ProcuracaoSerializer(serializers.ModelSerializer):
    days_to_expiry = serializers.IntegerField(source="days_to_expiry", read_only=True)

    class Meta:
        model = Procuracao
        fields = "__all__"
