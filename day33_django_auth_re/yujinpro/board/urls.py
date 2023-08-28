from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("main", views.main, name="main"),
    path("logout", views.logout_view, name="logout"),
]
