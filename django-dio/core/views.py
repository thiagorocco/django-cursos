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