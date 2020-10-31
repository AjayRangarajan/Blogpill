from django.urls import path
from . import views as blogs_views

app_name="blogs"

urlpatterns=[
    path("",blogs_views.blogs,name="blogs"),
    path("create_blog/",blogs_views.create_blog,name="create_blog"),
    path("<str:blog_id>/",blogs_views.blog_view,name="blog_view"),
]