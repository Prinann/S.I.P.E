from rest_framework import viewsets
from .models import Procuracao
from .serializers import ProcuracaoSerializer

class ProcuracaoViewSet(viewsets.ModelViewSet):
    queryset = Procuracao.objects.all().order_by("priority", "expiry_date")
    serializer_class = ProcuracaoSerializer
