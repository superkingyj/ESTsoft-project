from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)  # Char 필드: 글자형 데이터
    content = models.TextField()  # Text 필드
    published_date = models.DateTimeField()


class User(models.Model):
    user_id = models.CharField(max_length=32)
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length=64)
    register_date = models.DateField(auto_now_add=True)
    desc = models.TextField()
