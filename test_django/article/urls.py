from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'authors', AuthorViewSet)
urlpatterns = router.urls
