from django.core.management.base import BaseCommand, CommandError
from app.models import Cliente, Taxa, FilaEmail


def formata_email(cliente_nome, valor_total_taxas):
    return "Olá {}, no ano de 2018 você pagou R${} em taxas".format(
        cliente_nome, valor_total_taxas)
 

class Command(BaseCommand):
    help = 'Criar clientes pra executar o teste'

    def handle(self, *args, **options):
        import time
        inicio = time.time()        
        emails = []
        for cliente in Cliente.objects.all(): 
            valor_total_taxas = Taxa.total_taxa(cliente, '2018-01-01', '2018-12-31')
            email = FilaEmail(
                email=cliente.email, texto=formata_email(cliente.nome, valor_total_taxas))
            emails.append(email)
        print('vai comecar a criar')
        FilaEmail.objects.bulk_create(emails, batch_size=900)            
        fim = time.time()
        print('Executou em: ' + str(fim - inicio))