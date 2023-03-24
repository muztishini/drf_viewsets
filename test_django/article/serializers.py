from rest_framework import serializers
from .models import Article, Author


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "author", "title", "description", "body"]


class AuthorSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'name', 'articles']

    def get_articles(self, obj):
        queryset = Article.objects.filter(author=obj)
        return [ArticleSerializer(q).data for q in queryset]
