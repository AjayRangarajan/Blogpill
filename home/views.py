from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.models import User
from blogs.models import Blogs

def home(request):
    context = {
        'title': 'Blog app',
        'authors': User.objects.all(),
        'blogs': Blogs.objects.all(),
    }
    return render(request, 'home/home.html', context)

def about(request):
    context = {
        'title': 'About page',
    }
    return render(request, 'home/about.html', context)