from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.title, name="title"),
    path("search/", views.search, name="search"),
    path("add/", views.add, name="add"),
    path("edit/", views.edit, name="edit"),
    path("random/", views.rand, name="random")
]
