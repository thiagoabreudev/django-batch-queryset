from django.core.management.base import BaseCommand, CommandError
from app.models import Cliente, Taxa, FilaEmail
from datetime import datetime


def formata_email(cliente_nome, valor_total_taxas):
    return "Olá {}, no ano de 2018 você pagou R${} em taxas".format(
        cliente_nome, valor_total_taxas)


class Command(BaseCommand):

    def handle(self, *args, **options):
        data_inicio = datetime.now()
        import time
        inicio = time.time()
        for cliente in Cliente.objects.all(): 
            valor_total_taxas = Taxa.total_taxa(cliente, '2018-01-01', '2018-12-31')
            FilaEmail.objects.create(
                email=cliente.email, texto=formata_email(cliente.nome, valor_total_taxas))
        fim = time.time()
        print('Executou em: ' + str(fim - inicio))
        data_fim = datetime.now()
        print('inicio em {} e terminou em {}'.format(str(data_inicio), str(data_fim)))