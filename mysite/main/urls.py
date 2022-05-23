from operator import index
from django import views
from django.urls import path
from .views import index, home

# In VSC in urlpatterns don't use '/', because it is default in front of url.

urlpatterns = [
    path('<int:id>', index, name='index'),
    path("", home, name='home'),
]