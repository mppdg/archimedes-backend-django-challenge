"""archymedes_bk_challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.shortcuts import redirect
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from user_profile.views import Custom404View

schema_view = get_schema_view(
   openapi.Info(
      title="Archimydes Challenge API",
      default_version='v1',
   ),
    public=True,
    patterns=[path(r"^api/v1/", include(('user_profile.urls', "api"), namespace="v1"))],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('user_profile.urls')),
    path('api/docs', schema_view.with_ui('swagger', cache_timeout=0)),
    path('', lambda _: redirect('/api/docs')),
    re_path(r'^.*/$', Custom404View.as_view())
]
