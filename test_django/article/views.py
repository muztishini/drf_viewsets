from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
Простой ViewSet, предназначенный для перечисления или поиска пользователей.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
