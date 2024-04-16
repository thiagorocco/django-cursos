from django.shortcuts import HttpResponse, render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
def login_user(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
    else:
        redirect('/')
@login_required(login_url='/login/')
def titulo(request, id):
    evento = Evento.objects.get(id=id)
    return HttpResponse('<h1>Título do evento: {}</h1><h2>{}</h2>'.format(evento.titulo,evento.data_evento))
@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)