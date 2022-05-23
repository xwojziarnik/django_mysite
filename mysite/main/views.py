from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response, id):
    list_view = ToDoList.objects.get(id=id)
    name = list_view.name
    return render(response, template_name="main/index.html", context={"name": name})

def home(response):
    return render(response, template_name="main/home.html")
