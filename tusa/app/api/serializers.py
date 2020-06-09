from rest_framework import serializers
from ..models import Cocktail
from django.contrib.auth import get_user_model

User = get_user_model()


class CocktailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Cocktail
        fields = ["id", "title", "fortress", "description", "recipe", "picture", "rating", "author", "created_at"]
        read_only_fields = ["created_at"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username"]
