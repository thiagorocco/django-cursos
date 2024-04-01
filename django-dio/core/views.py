from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello, {} de {} anos</h1>'.format(nome, idade))

def soma(request, a, b):
    c = a + b
    return HttpResponse('<h1> A soma de {} + {} = {}</h1>'.format(a, b, c))

def mult(request, a, b):
    c = a * b
    return HttpResponse('<h1> A multiplicação de {} + {} = {}</h1>'.format(a, b, c))
def divi(request, a, b):
    try:
        c = a / b
        return HttpResponse('<h1> A divisão de {} + {} = {}</h1>'.format(a, b, c))
    except:
        return HttpResponse('<h1>Não pode dividir um número por zero!!!')

def subtr(request, a, b):
    c = a - b
    return HttpResponse('<h1> A subtração de {} + {} = {}</h1>'.format(a, b, c))