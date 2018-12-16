from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def posts_create(request):
    return HttpResponse("<h1>Create</h1>")
def posts_details(request): #retrieve
    return HttpResponse("<h1>Details</h1>")

def posts_list(request):    #list items
    return render(request, "index.html", {})

def posts_update(request):
    return HttpResponse("<h1>Update</h1>")

def posts_delete(request):
    return HttpResponse("<h1>Delete</h1>")