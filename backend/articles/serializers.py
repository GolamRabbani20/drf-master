from drf_api.serializers import UserPublicSerializer
from .models import Article
from rest_framework import serializers

class AriticleSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(source='user', read_only=True)
    class Meta:
        model = Article
        fields = [
            'pk',
            'author',
            'title',
            'body',
            'path',
            'endpoint'
        ]