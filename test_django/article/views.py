from rest_framework import viewsets
from .models import Article, Author
from .serializers import ArticleSerializer, AuthorSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
Простой ViewSet, предназначенный для перечисления или поиска пользователей.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
