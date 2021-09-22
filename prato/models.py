from django.db import models



class Prato(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
