from django.db import models


class user(models.Model):
    idUser = models.IntegerField()
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=70)
    tipo = models.IntegerField()

class pesquisa(models.Model):
    data = models.DateTimeField()
    idPesq = models.IntegerField()
    tempoCarreg = models.IntegerField()
    ping = models.IntegerField()

class site(models.Model):

    idSite = models.IntegerField()
    url = models.CharField(max_length=100)
    
    


    
