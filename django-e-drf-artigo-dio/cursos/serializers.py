from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacaofields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario'
            'avaliacao',
            'criacao',
            'ativo'
        )