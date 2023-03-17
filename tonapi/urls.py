"""tonapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from rest_framework import permissions
from tonapiapp import views
from tonapiapp.views import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf import settings 
from rest_framework.authtoken.views import obtain_auth_token

schema_view = get_schema_view(
   openapi.Info(
      title="Podo API",
      default_version='v4',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),    # admin page
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),    # setting swagger UI as home

    path("articles", ArticleViewSet.as_view({"get": "list"}), name="articles"),
    path('api-token-auth/', obtain_auth_token),

    # path("", UserDetailAPI.as_view()),
    path('register', RegisterUserAPIView.as_view()),
    
    path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
