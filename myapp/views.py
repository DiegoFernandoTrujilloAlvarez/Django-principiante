#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task


# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello World</h1>")

def about(resquest):
    return HttpResponse("<h1>About</h1>")

def hello2(request, username):
    return HttpResponse(f"<h1>Hello {username}</h1>")

def projects(request):
    p = list(Project.objects.values())
    return JsonResponse(p, safe=False)

def tasks(request, id):
    t = Task.objects.get(id=id)
    return HttpResponse(f"task: {t.title}")