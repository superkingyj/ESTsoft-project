from django.urls import path
from . import views

urlpatterns = [
    path("", views.google_login, name="login"),
    path("success", views.google_login_success, name="success"),
]
