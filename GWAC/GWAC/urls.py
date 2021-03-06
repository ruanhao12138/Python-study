"""GWAC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views import *
from datum import views
from django.conf import settings
import xadmin
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('xadmin/', xadmin.site.urls),
    path('data_add_form/', views.data_add_form, name='data_add_form'),
    path('datum/', include('datum.urls')),
    path('accounts/', include('user.urls')),
    path(r'search/', include('haystack.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
