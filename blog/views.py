from django.shortcuts import render
from .models import postBlog
# Create your views here.

def home(request):
    posts = postBlog.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'home.html', context)