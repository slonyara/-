from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Cocktail(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255
    )
    fortress = models.CharField(
        verbose_name="Крепость",
        max_length=255
    )
    description = models.TextField(
        verbose_name="Описание приготовления"
    )
    recipe = models.TextField(
        verbose_name="Рецепт"
    )
    picture = models.ImageField(
        "Изображение"
    )
    rating = models.PositiveSmallIntegerField(
        "Рейтинг",
        default=0
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        editable=False
    )
    updated_to = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detailed_view", kwargs={"pk": self.id})

    class Meta:
        verbose_name = "коктейль"
        verbose_name_plural = "коктейли"


class Evaluation(models.Model):
    user = models.ForeignKey(User, models.CASCADE, related_name='evaluation_user')
    cocktail = models.ForeignKey(Cocktail, models.CASCADE, related_name='evaluation_cocktail')
    evaluation = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.user.username}|{self.cocktail.title}|{self.evaluation}'

    class Meta:
        verbose_name = "оценка"
        verbose_name_plural = "оценки"
