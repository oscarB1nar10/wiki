from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>", views.title, name="wiki"),
    path("search/", views.searh, name="search")
]
