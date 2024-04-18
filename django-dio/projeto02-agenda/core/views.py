from django.shortcuts import HttpResponse, render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválido')
    return redirect('/')
@login_required(login_url='/login/')
def titulo(request, id):
    evento = Evento.objects.get(id=id)
    return HttpResponse('<h1>Título do evento: {}</h1><h2>{}</h2>'.format(evento.titulo,evento.data_evento))
@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento,'usuario':usuario}
    return render(request, 'agenda.html', dados)
@login_required(login_url='/login/')
def evento(request):
    usuario = request.user
    dados = {'usuario': usuario}
    return render(request, 'evento.html', dados)
@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        local = request.POST.get('local')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              local=local,
                              descricao=descricao,
                              usuario=usuario)
    return redirect('/')
@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    # cada usuário só vai excluir o que for seu
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')
