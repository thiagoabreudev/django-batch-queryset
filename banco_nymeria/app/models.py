from django.db import models
from django.db.models import Sum


class Cliente(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=255)
    email = models.EmailField(verbose_name="E-mail", max_length=255, default='contato@contato.com')

    class Meta:
        verbose_name = 'Cliente' 
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome




class Taxa(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="taxas")
    data = models.DateField(verbose_name="Data")
    valor = models.DecimalField(verbose_name="Valor", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Taxa' 
        verbose_name_plural = 'Taxas'
    
    def __str__(self):
        return self.cliente.nome

    def total_taxa(cliente, data_inicio, data_fim):
        return Taxa.objects.filter(
            cliente=cliente, data__gte=data_inicio, data__lte=data_fim).aggregate(Sum('valor'))

    


class FilaEmail(models.Model):
    email = models.EmailField(verbose_name="E-mail", max_length=255)
    texto = models.TextField(verbose_name="Texto")

    def __str__(self):
        return self.email
    

    