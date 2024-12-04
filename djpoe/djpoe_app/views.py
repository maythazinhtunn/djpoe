from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("About")

def add(request,num1,num2):
    return HttpResponse(num1+num2)

def info(request,name,age):
    info={
        "name": name,
        "age": age
    }
    return JsonResponse(info)