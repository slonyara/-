from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from app.api.views import UserViewSet, CocktailViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("cocktail", CocktailViewSet)


app_name = "api"
urlpatterns = router.urls
