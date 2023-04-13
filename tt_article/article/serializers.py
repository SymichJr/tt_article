from rest_framework import serializers

from .models import Article, User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'is_public')
        model = Article


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'email', 'password', 'role')
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data.get('role', User.SUBSCRIBER)
        )
        return user


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=User.AUTHOR
        )
        return user


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=User.AUTHOR
        )
        return user