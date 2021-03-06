from cgitb import text
from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.


def index(response, id):
    list_view = ToDoList.objects.get(id=id)

    if response.method == "POST":
        if response.POST.get("save"):
            for item in list_view.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                list_view.item_set.create(text=txt, complete=False)
            else:
                print("Invalid")
    return render(response, template_name="main/index.html", context={"list_view": list_view})

def home(response):
    return render(response, template_name="main/home.html")

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        
        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()
    return render(response, template_name="main/create.html", context={"form": form})
