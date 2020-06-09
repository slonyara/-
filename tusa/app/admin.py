from django.contrib import admin
from .models import Cocktail, Evaluation


@admin.register(Cocktail)
class CocktailAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ["user", "cocktail"]
