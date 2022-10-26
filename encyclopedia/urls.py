from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>", views.title, name="wiki"),
    path("search/", views.searh, name="search"),
    path("new_page/", views.new_page, name="new_page"),
    path("save_page/", views.save_page, name="save_page")
]
