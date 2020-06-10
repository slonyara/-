# import pytest
#
# from app.forms import UserCreationForm, CocktailAddForm
# from app.models import Cocktail
# from app.tests.factories import CocktailFactory
#
# pytestmark = pytest.mark.django_db
#
#
# class TestUserCreationForm:
#     def test_clean_username(self):
#         # A user with proto_user params does not exist yet.
#         proto_user = CocktailFactory.build()
#
#         form = CocktailAddForm(
#             {
#                 "title": proto_user.username,
#                 "password1": proto_user._password,
#                 "password2": proto_user._password,
#             }
#         )
#
#         assert form.is_valid()
#         assert form.clean_username() == proto_user.username
#
#         # Creating a user.
#         form.save()
#
#         # The user with proto_user params already exists,
#         # hence cannot be created.
#         form = UserCreationForm(
#             {
#                 "username": proto_user.username,
#                 "password1": proto_user._password,
#                 "password2": proto_user._password,
#             }
#         )
#
#         assert not form.is_valid()
#         assert len(form.errors) == 1
#         assert "username" in form.errors
