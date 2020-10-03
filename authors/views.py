from django.shortcuts import render
from authors.models import Authors
# from PIL import Image


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
    title=f"{author.name}-Profile"
    blogs=author.blogs.all()
    no_of_blogs=len(blogs)
    # img=open(author.profile_pic.url,'rb')
    # author_image = Image.open(img)
    # author_image.resize((400,400))
    # author_image.save()
    # # img.close()
    # print(author.profile_pic.url)
    context={
        "title":title,
        "author":author,
        "blogs":blogs,
        "no_of_blogs":no_of_blogs,
    }

    return render(request,"authors/author_profile.html",context)

