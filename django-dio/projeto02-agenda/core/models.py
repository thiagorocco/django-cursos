from django.db import models

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_cricao = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo