import pytest
from django.urls import resolve, reverse

from app.models import Cocktail
from django.contrib.auth import get_user_model

User = get_user_model()
pytestmark = pytest.mark.django_db


def test_detail():
    User.objects.create_user('foo', password='bar')
    Cocktail.objects.create(
        title='Test',
        fortress='ttt',
        description='fbcvbcvbc',
        recipe='gnfghg',
        picture='tуса_juice/static/1.jpg',
        author=User.objects.first()
    )
    cocktail = Cocktail.objects.first()

    assert (
        reverse("detailed_view", kwargs={"pk": cocktail.id})
        == f"/cocktail/{cocktail.id}"
    )
    assert resolve(f"/cocktail/{cocktail.id}").view_name == "detailed_view"


def test_add():
    assert reverse("add_view") == "/cocktail/add"
    assert resolve("/cocktail/add").view_name == "add_view"
