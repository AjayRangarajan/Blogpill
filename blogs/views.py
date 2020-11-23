from django.http import HttpResponse
from django.shortcuts import render,redirect
from blogs.models import Blogs
from authors.models import Authors
from blogs.forms import BlogCreationForm,BlogUpdateForm
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
# @allowed_users(allowed_groups=['Authors'])
@authors_only
def create_blog(request):
    if request.method=="POST":
        blog_creation_form=BlogCreationForm(request.POST,request.FILES)
        if blog_creation_form.is_valid():
            new_blog=blog_creation_form.save()
            author=Authors.objects.get(default=request.user)
            new_blog.author=author
            new_blog.save()
            messages.success(request,'successfully created the blog!')
            return redirect('blogs:blogs')
        else:
            messages.error(request,'please fill the form properly!')
            return redirect('blogs:create_blog')
    blog_creation_form=BlogCreationForm()
    context={
        'title':"Blog Editor",
        'blog_creation_form':blog_creation_form,
    }
    return render(request,"blogs/blog_editor.html",context)



def blog_view(request,blog_id):

    blog=Blogs.objects.get(pk=blog_id)

    context={
        'title':blog.title.capitalize(),
        'blog':blog,
    }
    return render(request,"blogs/blog_view.html",context)

@login_required(login_url='home:login_page')
# @allowed_users(allowed_groups=['Authors'])
@authors_only
def update_blog(request,blog_id):
    blog=Blogs.objects.get(pk=blog_id)
    blog_update_form=BlogUpdateForm(instance=blog)

    if request.method=="POST":
        blog_update_form=BlogUpdateForm(request.POST,instance=blog)
        if blog_update_form.is_valid():
            blog_update_form.save()
            messages.success(request,'successfully updated the blog!')
            return redirect('blogs:blog_view',blog_id=blog.id )
        else:
            messages.error(request,'something went wrong!')
            return redirect('blogs:update_blog',blog_id=blog.id)
    context={
        'title': "Update Blog",
        'blog_id': blog.id,
        'blog_update_form': blog_update_form,
    }
    return render(request,"blogs/blog_update_form.html",context)

@login_required(login_url='home:login_page')
# @allowed_users(allowed_groups=['Authors'])
@authors_only
def delete_blog(request,blog_id):
    blog=Blogs.objects.get(pk=blog_id)
    blog.delete()
    messages.info(request,'Blog deleted!')
    return redirect('blogs:blogs')