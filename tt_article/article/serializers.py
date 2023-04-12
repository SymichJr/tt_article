from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'is_public')
        model = Article