from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response, name):
    list_view = ToDoList.objects.get(name=name)
    item = list_view.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>"% (list_view.name, str(item.text)))
