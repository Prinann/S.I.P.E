from django.test import TestCase
from .models import Procuracao
from datetime import date, timedelta

class ProcuracaoTest(TestCase):
    def test_criacao_procuracao(self):
        p = Procuracao.objects.create(
            nome_cliente='João Silva',
            numero_procuracao='12345',
            data_vencimento=date.today() + timedelta(days=30)
        )
        self.assertEqual(str(p), 'João Silva - 12345')
