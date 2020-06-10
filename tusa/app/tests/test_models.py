import pytest

from app.models import Cocktail
from django.contrib.auth import get_user_model

User = get_user_model()

pytestmark = pytest.mark.django_db


def test_cocktail_get_absolute_url():
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
    assert cocktail.get_absolute_url() == f"/cocktail/{cocktail.id}"
