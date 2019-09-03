"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
from . import adress_from_zip as zip
from . import prefectures_api as pref
from . import municipalities_api as city

urlpatterns = [
    path(
        'admin/',
        admin.site.urls),
    path(
        'api/v1/addresses/zip/get',
        zip.AddressFromZip.as_view(),
        name='cls-v'),
    path(
        'api/v1/prefectures',
        pref.Prefectures.as_view(),
        name='pref-v'),
    path(
        'api/v1/cities',
        city.Municipalities.as_view(),
        name='city-v'),
    path(
        'api/v1/addresses/zip',
        views.get_address_from_zip,
        name='fnc-v'),
]
