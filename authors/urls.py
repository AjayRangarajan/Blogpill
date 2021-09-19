from django.urls import path 
from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.authors, name='authors'),
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('<int:user_id>/', views.view_profile, name='view_profile'),
    path('update_profile/<int:user_id>/', views.update_profile, name='update_profile'),
    path('delete_profile/<int:user_id>/', views.delete_profile, name='delete_profile'),
]
