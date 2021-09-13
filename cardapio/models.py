from django.db import models

class Cardapio(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.CharField(max_length=100)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome

