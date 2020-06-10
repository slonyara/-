from django.contrib.auth import forms, get_user_model
from django.utils.translation import ugettext_lazy as _
from .models import Cocktail, Evaluation
from django import forms as forms_django

User = get_user_model()


class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])


class CocktailAddForm(forms_django.ModelForm):
    class Meta:
        model = Cocktail
        fields = ["title", "fortress", "description", "recipe", "picture"]


class AddRatingForm(forms_django.ModelForm):
    evaluation = forms_django.IntegerField(max_value=5, min_value=0, required=True, label='Рейтинг(от 0 до 5)')

    class Meta:
        model = Evaluation
        fields = ['evaluation']
