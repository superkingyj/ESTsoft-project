from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("oreumi", views.new_page, name="page"),
    path("oreumi2", views.new_page2, name="page2"),
    path("my_page", views.my_page, name="my_page"),
]
