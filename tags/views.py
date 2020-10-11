from django.shortcuts import render,HttpResponse
from tags.models import Tags

def tags(request):
    tags=Tags.objects.all()
    context={
        'title':"Tags",
        'tags':tags,
    }
    return render(request,"tags/tags.html",context)

def tag_view(request,tag_name):

    tag=Tags.objects.get(name=tag_name)
    blogs=tag.blogs.all()
    no_of_blogs=len(blogs)

    context={
        'title': tag.name,
        'blogs': blogs,
        'tag':tag,
        'no_of_blogs':no_of_blogs,
    }
    return render(request,"tags/tag_view.html",context)