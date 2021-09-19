from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:pk>/',views.view_blog, name='view_blog'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('update_blog/<int:blog_id>/', views.update_blog, name='update_blog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]
