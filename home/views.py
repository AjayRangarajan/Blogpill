from django.shortcuts import render,redirect
from django.http import HttpResponse
from blogs.models import Blogs
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):

    all_blogs=Blogs.objects.all()
    featured_blogs=[]

    groups=None
    is_author=False
    if request.user.is_authenticated:
        if request.user.groups.exists():
            groups=request.user.groups.all()
            for group in groups:
                if group.name == 'Authors':
                    is_author=True
    
    for blog in all_blogs:
        if blog.was_published_recently():
            featured_blogs.append(blog)

    context={
        'title':'HOME',
        'featured_blogs':featured_blogs,
        'is_author':is_author,
    }
    return render(request,"home/home.html",context)

def login_view(request):
    if request.method == "POST":
        login_user=request.POST.get('login-name')
        login_password=request.POST.get('login-password')
        user=authenticate(username=login_user,password=login_password)
        if user != None:
            login(request,user)
            return redirect('home:home')
        else:
            return HttpResponse("Invalid credentials!!")
    
    context={
        'title':"LOGIN PAGE",
    }
    return render(request,"home/login_page.html",context)

@login_required(login_url='home:login_page')
def logout_view(request):
    logout(request)
    return redirect('home:home')