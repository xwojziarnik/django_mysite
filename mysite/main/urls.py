from operator import index
from django.urls import path
from .views import index, v1

urlpatterns = [
    path('', index, name='index'),
    path('v1', v1, name='v1'),
]