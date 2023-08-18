from django.urls import path
from . import views

urlpatterns = [
    path("", views.read_Post_data, name="index"),
    path("add_page", views.add_Post_data, name="add_data"),
    path("add_user_info", views.add_User_data, name="add_user_data"),
    path(
        "success_user_info", views.add_User_data_success, name="add_user_data_success"
    ),
]
