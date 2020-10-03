from django.urls import path
from . import views as blogs_views

app_name="blogs"

urlpatterns=[
    path("",blogs_views.blogs,name="blogs"),
    path("<str:blog_name>/",blogs_views.blog_view,name="blog_view")
]