from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    descricao = models.CharField(max_length=255)
    
    def __str__(self):
        return self.descricao

class Editora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()
    
    def __str__(self):
        return self.nome
    
class Autor(models.Model):
    class Meta:
        verbose_name_plural = "autores"
        
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    
    titulo = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=32)
    quantidade = models.IntegerField(default=1)
    preco = models.FloatField(default=1.0)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros", default=1)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros",default=1)
    autores = models.ManyToManyField(Autor, related_name="livros")
    
    def __str__(self):
        return "%s (%s)" %(self.titulo, self.editora)

class Compra(models.Model):
    
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        REALIZADO = 2, 'Realizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'
        
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compras") 
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)   