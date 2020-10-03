from django.urls import path
from . import views as authors_views

app_name="authors"

urlpatterns=[
    path("",authors_views.authors,name="authors"),
    path("<int:author_id>/",authors_views.author_profile,name="author_profile"),
]