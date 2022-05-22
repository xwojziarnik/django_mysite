from operator import index
from django.urls import path
from .views import index

# In VSC in urlpatterns don't use '/', because it is default in front of url.

urlpatterns = [
    path('<str:name>', index, name='index'),
]