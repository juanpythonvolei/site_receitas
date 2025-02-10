from django.db import models

# Create your models here.

class Receitas(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.CharField(blank=True, null=True,max_length=100)
    nome = models.CharField(blank=True, null=True,max_length=100)
    data = models.CharField(blank=True, null=True,max_length=100)
    infos = models.CharField(blank=True, null=True,max_length=10000)
    tipo = models.CharField(blank=True, null=True,max_length=100)

    class Meta:
        db_table = 'Receitas'




class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(blank=True, null=True,max_length=100)
    senha = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Usuarios'
