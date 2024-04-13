from django.shortcuts import render
from models import Evento

# Create your views here.
def titulo_evento():
    evento = Evento.objects.all()