from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer

from core.models import Categoria

import json

def teste(request):
    return HttpResponse('Olá, mundo do Django')

def teste2(request):
    return HttpResponse('Página 2')


@method_decorator(csrf_exempt, name="dispatch")
class CategoriaView(View):
    def get(self, request, id=None):
        if id:
            qs = Categoria.objects.get(id=id)
            data = {}
            data['id'] = qs.id
            data['descricao'] = qs.descricao
            return JsonResponse(data)
        
        data = list(Categoria.objects.values())
        formated_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(formated_data, content_type="application/json")
    
    def post(self, request):
        json_data = json.loads(request.body) # o dado que está vindo
        nova_categoria = Categoria.objects.create(**json_data)
        data = {"id":nova_categoria.id, "descricao":nova_categoria.descricao}
        return JsonResponse(data)
    
    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Categoria.objects.get(id=id)
        qs.descricao = json_data['descricao']
        qs.save()
        data = {}
        data['id'] = qs.id
        data['descricao'] = qs.descricao
        return JsonResponse(data)
    
    def delete(self, request, id):
        qs = Categoria.objects.get(id=id)
        qs.delete()
        data = {'mensagem': "Item excluído com sucesso."}
        return JsonResponse(data)

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class CategoriasList(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriaDetail(APIView):
    def get(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    
    def put(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):    
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)