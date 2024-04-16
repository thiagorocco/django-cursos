from django.shortcuts import HttpResponse, render
from core.models import Evento
from django.contrib.auth.decorators import login_required

def login_user(request):
    return render(request, 'login.html')
@login_required(login_url='/login/')
def titulo(request, id):
    evento = Evento.objects.get(id=id)
    return HttpResponse('<h1>Título do evento: {}</h1><h2>{}</h2>'.format(evento.titulo,evento.data_evento))
@login_required(login_url='/login/')
def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)