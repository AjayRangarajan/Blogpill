from django.shortcuts import render
from blogs.models import Blogs
# from django.core.paginator import Paginator

def blogs(request):

    blogs=Blogs.objects.all()
    # p=Paginator(blogs,10)

    context={
        "title":"BLOGS",
        "blogs":blogs,
    }
    return render(request,"blogs/blogs.html",context)

def blog_view(request,blog_name):

    blog=Blogs.objects.get(blog_name=blog_name)

    context={
        'title':blog.blog_title.capitalize(),
        'blog':blog,
    }
    return render(request,"blogs/blog_view.html",context)