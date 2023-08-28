# 

## 관리자 페이지 커스터마이징하기
```python
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```
1. app/models.py 작성

```python
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Article)
```
2. app/admin.py 작성

![](https://velog.velcdn.com/images/superkingyj/post/6fc7cba0-ca67-467c-bad2-a5c670df1f9e/image.png)
3. localhost:8000/admin 페이지 들어가보기

```python
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_at"]
    list_filter = ("title", "content", "created_at")

# Article 모델을 ArticleAdmin으로 커스텀하여 admind을 등록하겠다
admin.site.register(Article, ArticleAdmin)
```
4. app/admin.py 수정

![](https://velog.velcdn.com/images/superkingyj/post/9d608ae1-3549-436f-8e54-92d3586963cb/image.png)
5. 필터 확인

<br>

## 장고 꾸미기
```$ pip install django-grappelli```
1. 설치

```python
INSTALLED_APPS = [
    "grappelli",
    ...
]
...
STATIC_URL = "static/"
STATIC_ROOT = "static"
```
2. installed app에 추가

```
$ python manage.py collectstatic
```
3. 적용

![](https://velog.velcdn.com/images/superkingyj/post/dcf00b7d-6172-4d45-8d4b-f88b750cbf3d/image.png)
4. admim에서 확인