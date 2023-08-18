from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("create", views.article_create, name="article_create"),
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("signup", views.signup, name="signup"),
]
