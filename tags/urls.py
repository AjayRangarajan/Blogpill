from django.urls import path
from . import views as tags_views

app_name="tags"

urlpatterns=[
    path("",tags_views.tags,name="tags"),
    # path("<str:tag_name>/",tags_views.tag_view,name="tag_view"),
]