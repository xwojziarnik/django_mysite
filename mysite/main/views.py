from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("Hello on my index site.")

def v1(response):
    return HttpResponse("View number 1")
