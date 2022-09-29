from django.contrib.auth.models import User
from rest_framework import serializers
from .models import mensagem


class MessageSerializer(serializers.ModelSerializer):
    emissor = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receptor = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    class Meta:
        model = mensagem
        fields = ['emissor', 'receptor', 'conteudo', 'timestamp']
class ChatSerializer(serializers.ModelSerializer):
    emissor = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receptor = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    class Meta:
        model = mensagem
        fields = ['emissor', 'receptor', 'conteudo', 'timestamp']