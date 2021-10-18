from django.db import models
from prato.models import Prato

class Pedido(models.Model):
    pratos = models.ManyToManyField(Prato)
    quantidade = models.IntegerField(blank=True, null=True)
    mesa = models.IntegerField(blank=True, null=True)
    observacao = models.CharField(max_length=100)

    def __str__(self):
        return self.mesa


class Deliver(models.Model):
    pratos = models.ManyToManyField(Prato)
    quantidade = models.IntegerField(blank=True, null=True)
    local = models.CharField(max_length=100)
    observacao = models.CharField(max_length=100)


    def __str__(self):
        return self.local
