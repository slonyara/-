import pytest
from django.contrib.auth import get_user_model
# from app.tests.factories import CocktailFactory
# from app.models import Cocktail

# User = get_user_model()


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


# @pytest.fixture
# def cocktail() -> Cocktail:
#     return CocktailFactory()
