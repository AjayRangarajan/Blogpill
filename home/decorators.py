from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages


def allowed_users(allowed_groups=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            groups=None
            allow=False
            if request.user.groups.exists():
                groups=request.user.groups.all()
                for group in groups:
                    if group.name in allowed_groups:
                        allow=True
                if allow:
                    return view_func(request,*args,**kwargs)
                else:
                    return HttpResponse("You have no permissions to view this page!")
            else:
                return HttpResponse("You have no permissions to view this page")
        return wrapper_func
    return decorator

def authors_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        groups=None
        allow=False
        if request.user.groups.exists():
            groups=request.user.groups.all()
            for group in groups:
                if group.name == "Authors":
                    allow=True
            if allow:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("You have no permissions to view this page!")
        else:
            return HttpResponse("You have no permissions to view this page")
    return wrapper_func