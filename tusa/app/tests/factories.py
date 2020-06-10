# from typing import Any, Sequence
# from app.models import Cocktail
# from factory import DjangoModelFactory, Faker, post_generation
#
#
# class CocktailFactory(DjangoModelFactory):
#
#     username = Faker("user_name")
#     email = Faker("email")
#     name = Faker("name")
#
#     @post_generation
#     def password(self, create: bool, extracted: Sequence[Any], **kwargs):
#         password = (
#             extracted
#             if extracted
#             else Faker(
#                 "password",
#                 length=42,
#                 special_chars=True,
#                 digits=True,
#                 upper_case=True,
#                 lower_case=True,
#             ).generate(extra_kwargs={})
#         )
#         self.set_password(password)
#
#     class Meta:
#         model = Cocktail
#         django_get_or_create = ["username"]
