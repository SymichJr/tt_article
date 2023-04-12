from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import(
    ArticleAllViewSet,
    ArticleSubscriberViewSet,
    ArticleAuthorViewSet,
    UserListView,
    SubscriberCreateView,
    AuthorCreateView,
)

router = DefaultRouter()
router.register(r"articles", ArticleAllViewSet, basename="articles")
router.register(r"articles_sub", ArticleSubscriberViewSet, basename="articles_sub")
router.register(r"articles/(?P<article_id>\d+)", ArticleAuthorViewSet, basename="article_author")


urlpatterns = [
    path("", include(router.urls)),
    path("users/", UserListView.as_view()),
    path("subscribers/", SubscriberCreateView.as_view()),
    path('authors/', AuthorCreateView.as_view())
]