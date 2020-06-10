"""tyca_juice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import (
    main,
    detailed_view,
    remove_view,
    user_creation_view,
    cocktail_creation_view,
    add_rating,
    cocktail_update_view,
    search
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

login_view = auth_views.LoginView.as_view(
    template_name='form.html'
)

schema_view = get_schema_view(
    openapi.Info(
        title="tyca juice API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
      path('', main, name="main"),
      path('cocktail/add', cocktail_creation_view, name="add_view"),
      path('search/', search, name="search_view"),
      path('cocktail/remove/<int:pk>/', remove_view, name="remove_view"),
      path('cocktail/edit/<int:pk>/', cocktail_update_view, name="cocktail_update_view"),
      path('cocktail/add/rating/<int:pk>/', add_rating, name="add_rating_view"),
      path('cocktail/<int:pk>', detailed_view, name="detailed_view"),
      path('admin/', admin.site.urls),
      path('login/', login_view, name='login'),
      path("logout/", view=auth_views.LogoutView.as_view(), name="logout"),
      path("registration/", view=user_creation_view, name="registration"),
      path("api/docs/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
      path("api/v1/", include("app.api.api_urls")),
      # path('accounts/', include('django.contrib.auth.urls')),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()
