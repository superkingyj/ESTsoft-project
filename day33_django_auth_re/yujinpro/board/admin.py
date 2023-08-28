from django.contrib import admin
from .models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_at"]
    list_filter = ("title", "content", "created_at")

# Article 모델을 ArticleAdmin으로 커스텀하여 admind을 등록하겠다
admin.site.register(Article, ArticleAdmin)
