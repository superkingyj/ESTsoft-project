from . import views
from django.urls import path

urlpatterns = [
    path("", views.login, name="login"),
 
    path("article_list", views.article_list, name="article_list"),
    path("create", views.article_create, name="article_create"),
    
    path("sign_up", views.sign_up, name="sign_up"),
    path("logout", views.logout_view, name="logout"),
    
    path("login_success", views.login_success, name="login_success")
]
