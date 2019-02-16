from django.core.management.base import BaseCommand, CommandError
from app.models import Cliente
import uuid


class Command(BaseCommand):
    help = 'Criar clientes pra executar o teste'

    def handle(self, *args, **options):
        count = 0
        clientes = []
        for i in range(0, 500000):
            cliente = Cliente()
            cliente.nome = uuid.uuid1().hex
            count += 1
            clientes.append(cliente)
            if count == 1000:
                Cliente.objects.bulk_create(clientes)
                print('inseri: ' + str(i))
                clientes.clear()
                count = 0