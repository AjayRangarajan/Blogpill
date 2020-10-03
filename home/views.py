from django.shortcuts import render
from blogs.models import Blogs

def home(request):

    all_blogs=Blogs.objects.all()
    featured_blogs=[]
    
    for blog in all_blogs:
        if blog.was_published_recently():
            featured_blogs.append(blog)

    context={
        'title':'HOME',
        'featured_blogs':featured_blogs,
    }
    return render(request,"home/home.html",context)
