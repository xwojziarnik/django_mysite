from operator import index
from django.urls import path
from . import views


urlspatterns = [
    path("", views.index)
]