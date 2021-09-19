from django.urls import path
from . import views as home_views

app_name = "home"

urlpatterns=[
    path('', home_views.home, name="home"),
    path('about/', home_views.about, name="about"),
]