from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Post

def posts_create(request):
    return HttpResponse("<h1>Create</h1>")
def posts_details(request): #retrieve
    instance = get_object_or_404(Post, id=1)
    context = {
        "title" : instance.title,
        "instance" : instance,
    }
    return render(request, "post_detail.html", context)

def posts_list(request):   #list items

    queryset = Post.objects.all()
    context = {
        "object_list" : queryset,
        "title" : "List"

    }
    return render(request, "index.html", context)

    """
        if request.user.is_authenticated():
            context = {
                "title" : "My User List"
            }
        else:
            context = {
                "title" : "List"
            }
        return render(request, "index.html", context)
    """

def posts_update(request):
    return HttpResponse("<h1>Update</h1>")

def posts_delete(request):
    return HttpResponse("<h1>Delete</h1>")