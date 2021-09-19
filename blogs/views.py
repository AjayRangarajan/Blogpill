from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . models import Blogs
from .forms import BlogCreationForm, BlogUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def blogs(request):
    blogs = Blogs.objects.all()
    context = {
        'title': 'Blogs',
        'blogs': blogs,
    }
    return render(request, 'blogs/blogs.html', context)

def view_blog(request,pk):
    blog = Blogs.objects.get(pk=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blogs/view_blog.html', context)

@login_required(login_url='authors:login')
def create_blog(request):
    form = BlogCreationForm()
    if request.method == 'POST':
        form = BlogCreationForm(request.POST,request.FILES)
        if form.is_valid():
            new_blog = form.save()
            user = request.user
            new_blog.author = user
            new_blog.save()
            messages.success(request, f'successfully created the blog')
            return redirect('blogs:view_blog', pk=new_blog.pk)
        else:
            messages.error(request, 'Please fill the form properly!!!')
            return redirect('blogs:create_blog')
    context = {
        'title': "Blog Creation Form",
        'form': form,
    }
    return render(request, 'blogs/blog_editor.html',context)

@login_required(login_url='authors:login')
def update_blog(request, blog_id):
    blog = Blogs.objects.get(id = blog_id)
    if request.user != blog.author:
        return HttpResponse("You have no permission to edit this blog!!!")
    form = BlogUpdateForm(instance=blog)
    if request.method == 'POST':
        form = BlogUpdateForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully updated the blog!!!')
            return redirect('blogs:view_blog',pk=blog.pk)
        else:
            messages.error(request,'Please fill the form properly!!!')
            return redirect('blogs:update_blog',blog_id=blog_id)
    context = {
        'title': "UPDATE BLOG",
        'form': form,
        'blog_id': blog_id,
    }
    return render(request, 'blogs/update_blog.html',context)


@login_required(login_url='authors:login')
def delete_blog(request, blog_id):
    blog = Blogs.objects.get(id=blog_id)
    if request.user != blog.author:
        return HttpResponse("You have no permission to delete this blog!!!")
    blog.delete()
    messages.info(request,'successfully deleted the blog!!!')
    return redirect('blogs:blogs')





















# from django.http import HttpResponse
# from django.shortcuts import render,redirect
# from blogs.models import Blogs
# from authors.models import Authors
# from blogs.forms import BlogCreationForm,BlogUpdateForm
# from django.contrib.auth.decorators import login_required
# # from home.decorators import allowed_users,authors_only
# from django.contrib import messages
# # from django.core.paginator import Paginator

# def blogs(request):

#     blogs=Blogs.objects.all()
#     # p=Paginator(blogs,10)

#     context={
#         "title":"BLOGS",
#         "blogs":blogs,
#     }
#     return render(request,"blogs/blogs.html",context)


# @login_required(login_url='home:login_page')
# # @allowed_users(allowed_groups=['Authors'])
# @authors_only
# def create_blog(request):
#     if request.method=="POST":
#         blog_creation_form=BlogCreationForm(request.POST,request.FILES)
#         if blog_creation_form.is_valid():
#             new_blog=blog_creation_form.save()
#             author=Authors.objects.get(default=request.user)
#             new_blog.author=author
#             new_blog.save()
#             messages.success(request,'successfully created the blog!')
#             return redirect('blogs:blogs')
#         else:
#             messages.error(request,'please fill the form properly!')
#             return redirect('blogs:create_blog')
#     blog_creation_form=BlogCreationForm()
#     context={
#         'title':"Blog Editor",
#         'blog_creation_form':blog_creation_form,
#     }
#     return render(request,"blogs/blog_editor.html",context)



# def blog_view(request,blog_id):

#     blog=Blogs.objects.get(pk=blog_id)

#     context={
#         'title':blog.title.capitalize(),
#         'blog':blog,
#     }
#     return render(request,"blogs/blog_view.html",context)

# @login_required(login_url='home:login_page')
# # @allowed_users(allowed_groups=['Authors'])
# @authors_only
# def update_blog(request,blog_id):
#     blog=Blogs.objects.get(pk=blog_id)
#     blog_update_form=BlogUpdateForm(instance=blog)

#     if request.method=="POST":
#         blog_update_form=BlogUpdateForm(request.POST,instance=blog)
#         if blog_update_form.is_valid():
#             blog_update_form.save()
#             messages.success(request,'successfully updated the blog!')
#             return redirect('blogs:blog_view',blog_id=blog.id )
#         else:
#             messages.error(request,'something went wrong!')
#             return redirect('blogs:update_blog',blog_id=blog.id)
#     context={
#         'title': "Update Blog",
#         'blog_id': blog.id,
#         'blog_update_form': blog_update_form,
#     }
#     return render(request,"blogs/blog_update_form.html",context)

# @login_required(login_url='home:login_page')
# # @allowed_users(allowed_groups=['Authors'])
# @authors_only
# def delete_blog(request,blog_id):
#     blog=Blogs.objects.get(pk=blog_id)
#     blog.delete()
#     messages.info(request,'Blog deleted!')
#     return redirect('blogs:blogs')