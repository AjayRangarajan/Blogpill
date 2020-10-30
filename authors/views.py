from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from authors.models import Authors
from django.contrib import messages


def authors(request):

    authors=Authors.objects.all()        
    context={
        "title":"AUTHORS",
        "authors":authors,
    }
    return render(request,"authors/authors.html",context)    

def author_profile(request,author_id):
    author_id=int(author_id)
    author=Authors.objects.get(pk=author_id)
    title=f"{author.default.username}-Profile"
    blogs=author.blogs.all()
    no_of_blogs=len(blogs)
    context={
        "title":title,
        "author":author,
        "blogs":blogs,
        "no_of_blogs":no_of_blogs,
    }

    return render(request,"authors/author_profile.html",context)