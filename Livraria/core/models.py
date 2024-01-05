from django.db import models

# Create your models here.
class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

class Editora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()
