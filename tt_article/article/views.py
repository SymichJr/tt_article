from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .models import Article, User
from .pagination import StandardPagination
from .permissions import IsAuthorOrReadOnly
from .serializers import (ArticleSerializer, AuthorSerializer,
                          SubscriberSerializer, UserSerializer)


class ArticleAllViewSet(ReadOnlyModelViewSet):
    queryset = Article.objects.filter(is_public=True)
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardPagination


class ArticleSubscriberViewSet(ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardPagination


class ArticleAuthorViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        article = get_object_or_404(
            Article,
            pk = self.kwargs.get('article_id'),
        )
        serializer.save(
            author=self.request.user,
            article=article
        )
    
    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(ArticleAuthorViewSet)
    
    def perform_destroy(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("Изменение чужого контента запрещено!")
        serializer.delete()


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class SubscriberCreateView(APIView):
    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorCreateView(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)