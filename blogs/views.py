from django.http import HttpResponse
from django.shortcuts import render,redirect
from blogs.models import Blogs
from authors.models import Authors
from blogs.forms import BlogCreationForm
from django.contrib.auth.decorators import login_required
from home.decorators import allowed_users,authors_only
from django.contrib import messages
# from django.core.paginator import Paginator

def blogs(request):

    blogs=Blogs.objects.all()
    # p=Paginator(blogs,10)

    context={
        "title":"BLOGS",
        "blogs":blogs,
    }
    return render(request,"blogs/blogs.html",context)


@login_required(login_url='home:login_page')
@allowed_users(allowed_groups=['Authors'])
def create_blog(request):
    if request.method=="POST":
        blog_creation_form=BlogCreationForm(request.POST,request.FILES)
        if blog_creation_form.is_valid():
            new_blog=blog_creation_form.save()
            author=Authors.objects.get(default=request.user)
            new_blog.author=author
            new_blog.save()
            return redirect('home:home')
        else:
            return HttpResponse("something went wrong!")
    blog_creation_form=BlogCreationForm()
    context={
        'title':"Blog Editor",
        'blog_creation_form':blog_creation_form,
    }
    return render(request,"blogs/blog_editor.html",context)



def blog_view(request,blog_name):

    blog=Blogs.objects.get(name=blog_name)

    context={
        'title':blog.title.capitalize(),
        'blog':blog,
    }
    return render(request,"blogs/blog_view.html",context)