from django.urls import path
from . import views as home_views

app_name="home"

urlpatterns=[
    path("",home_views.home,name="home"),
    path("login/",home_views.login_view,name="login_page"),
    path("logout/",home_views.logout_view,name="logout_page"),
]