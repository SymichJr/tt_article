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

router = DefaultRouter
router.register(r"articles", ArticleAllViewSet)
router.register(r"articles_sub", ArticleSubscriberViewSet)
router.register(r"articles/(?P<article_id>\d+)", ArticleAuthorViewSet)
router.register(r"users", UserListView)
router.register(r"subscribers", SubscriberCreateView)
router.register(r"authors", AuthorCreateView)


urlpatterns = [
    path("", include(router.urls)),
]