from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    re_path("(?P<path>.*)", views.kwh_proxy, name="kwh"),
]
