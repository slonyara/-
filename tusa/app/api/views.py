from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from django_filters import rest_framework as filters
from rest_framework import filters as filters_django
from rest_framework import permissions

from .serializers import UserSerializer, CocktailSerializer
from ..models import Cocktail
from .permissions import IsAdminCocktail

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class CocktailFilter(filters.FilterSet):
    min_rating = filters.NumberFilter(field_name="rating", lookup_expr='gte')
    max_rating = filters.NumberFilter(field_name="rating", lookup_expr='lte')

    class Meta:
        model = Cocktail
        fields = ['author', 'min_rating', 'max_rating']


class CocktailViewSet(ModelViewSet):
    serializer_class = CocktailSerializer
    queryset = Cocktail.objects.all()
    permission_classes = (IsAdminCocktail, permissions.AllowAny)
    filter_backends = (filters.DjangoFilterBackend, filters_django.SearchFilter)
    filterset_class = CocktailFilter
    search_fields = ('title', 'fortress', 'description', 'recipe')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
