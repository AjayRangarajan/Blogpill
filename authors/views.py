from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'{user} created Succcessfully!')
            return redirect('authors:login')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('authors:register')
    form = UserRegistrationForm()
    context = {
        'title': 'Registration Page',
        'form': form,
    }
    return render(request, 'authors/registration.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            messages.success(request, f'successfully logged in as {username}')
            return redirect('home:home')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('authors:login')
    context = {
        'title': "LOGIN",
    }
    return render(request, 'authors/login.html', context)

@login_required(login_url='authors:login')
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out!')
    return redirect('home:home')

def authors(request):
    authors = User.objects.all()
    context = {
        'title': 'AUTHORS',
        'authors':authors,
    }
    return render(request,'authors/authors.html',context)

def view_profile(request,user_id):
    author = User.objects.get(id=user_id)
    context = {
        'title': f'{author.username}\'s Profile',
        'author': author,
    }
    return render(request,'authors/author_profile.html',context)


@login_required(login_url='authors:login')
def update_profile(request, user_id):
    user = User.objects.get(id=user_id)
    if request.user == user:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

        if request.method == 'POST':
            user_update_form = UserUpdateForm(request.POST,instance=request.user)
            profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if user_update_form.is_valid() and profile_update_form.is_valid():
                user_update_form.save()
                profile_update_form.save()
                messages.success(request,f'successfully updated the {request.user.username}\'s profile')
                return redirect('authors:view_profile',user_id=request.user.id)
            else:
                messages.error(request,'Please fill the data properly!!!')
                return redirect('authors:update_profile',user_id=request.user.id)
        context = {
            'title': "Update User Profile",
            'user_update_form': user_update_form,
            'profile_update_form': profile_update_form,
        }
        return render(request, 'authors/update_profile.html',context)
    else:
        return HttpResponse("You have no permission to edit this profile!!!")

@login_required(login_url='authors:login')
def delete_profile(request, user_id):
    author = User.objects.get(id = user_id)
    if request.user == author:
        author.delete()
        return redirect('authors:authors')
    else:
        return HttpResponse("You have no permission to delete this Profile")







# from django.http import HttpResponse
# from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User
# from authors.models import Authors


# def authors(request):

#     authors=Authors.objects.all()
#     context={
#         "title":"AUTHORS",
#         "authors":authors,
#     }
#     return render(request,"authors/authors.html",context)    

# def author_profile(request,author_id):
#     author_id=int(author_id)
#     author=Authors.objects.get(pk=author_id)
#     title=f"{author.default.username}-Profile"
#     blogs=author.blogs.all()
#     no_of_blogs=len(blogs)
#     context={
#         "title":title,
#         "author":author,
#         "blogs":blogs,
#         "no_of_blogs":no_of_blogs,
#     }

#     return render(request,"authors/author_profile.html",context)