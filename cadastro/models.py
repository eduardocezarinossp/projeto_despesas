from django.db import models

# Create your models here.
from django.utils import timezone

class Conta(models.Model) :
    descricao = models.CharField(max_length=50)
    valor = models.DecimalField
    data = models.CharField(max_length=50)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    responsavel = models.CharField(max_length=50)
    def __str__(self):
        return self.descricao

class Item(models.Model) :
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome