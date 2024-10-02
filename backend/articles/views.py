from rest_framework import generics
from .models import Article
from .serializers import AriticleSerializer

class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.public()
    serializer_class = AriticleSerializer

class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.public()
    serializer_class = AriticleSerializer