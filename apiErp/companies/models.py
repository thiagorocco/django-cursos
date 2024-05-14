from django.db import models
from accounts.models import User


# Create your models here.
class Enterprise(models.Model):
    name = models.CharField(max_length=175)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #integridade referencial
