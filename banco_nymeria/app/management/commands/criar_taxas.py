from django.core.management.base import BaseCommand, CommandError
from app.models import Cliente, Taxa
import uuid
from random import random

class Command(BaseCommand):
    help = 'Criar clientes pra executar o teste'

    def handle(self, *args, **options):
        for cliente in Cliente.objects.all(): 
            taxa1 = '%0.2f' %( random())
            taxa2 = '%0.2f' %( random())
            taxa3 = '%0.2f' %( random())
            Taxa.objects.bulk_create(
                [
                    Taxa(cliente=cliente, valor=taxa1, data='2018-10-10'),
                    Taxa(cliente=cliente, valor=taxa1, data='2018-10-10'),
                    Taxa(cliente=cliente, valor=taxa1, data='2018-10-10')
                ]
            )
            print('Criando taxa para cliente: {}'.format(cliente.nome))
