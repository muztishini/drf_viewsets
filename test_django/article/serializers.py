from rest_framework import serializers
from .models import Article, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ("id", "title", "description", "body", "author")

    # def create(self, validated_data):
    #     author = validated_data.pop('author')
    #     article = Article.objects.create(**validated_data)
    #     Author.objects.create(author=author, article=article)
    #     return article
