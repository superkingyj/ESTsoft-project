from django.urls import path, include
from .views import ProductAPIView


urlpatterns = [
    path('products/', ProductAPIView.as_view())
]