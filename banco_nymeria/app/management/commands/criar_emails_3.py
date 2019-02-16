from django.core.management.base import BaseCommand
from app.models import Cliente, Taxa, FilaEmail


def formata_email(cliente_nome, valor_total_taxas):
    return "Olá {}, no ano de 2018 você pagou R${} em taxas".format(
        cliente_nome, valor_total_taxas)


# O queryset dividido para nao consumir muita memoria, devido a quantidade de dados
def batch_qs(qs, batch_size=1000):
    """
    Returns a (start, end, total, queryset) tuple for each batch in the given
    queryset.
    """
    total = qs.count()
    for start in range(0, total, batch_size):
        end = min(start + batch_size, total)
        yield (start, end, total, qs[start:end])


class Command(BaseCommand):
    def handle(self, *args, **options):
        import time
        inicio = time.time()        
        emails = []
        cliente_qs = Cliente.objects.all()
        for start, end, total, qs in batch_qs(cliente_qs, batch_size=1000):
            print("Novo processamento %s - %s de %s" % (start + 1, end, total))            
            for cliente in qs:
                valor_total_taxas = Taxa.total_taxa(cliente, '2018-01-01', '2018-12-31')
                email = FilaEmail(
                    email=cliente.email, texto=formata_email(cliente.nome, valor_total_taxas))         
                emails.append(email)            
            FilaEmail.objects.bulk_create(emails)
            emails.clear()
        fim = time.time()
        print('Executou em: ' + str(fim - inicio))