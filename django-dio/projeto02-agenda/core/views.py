from django.shortcuts import HttpResponse
from core.models import Evento

def titulo(request, id):
    evento = Evento.objects.get(id=id)
    return HttpResponse('<h1>Título do evento: {}</h1><h2>{}</h2>'.format(evento.titulo,evento.data_evento))