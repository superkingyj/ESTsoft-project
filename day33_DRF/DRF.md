# DRF

## DRF
- Django 기반으로 웹 API 개발을 위한 프레임워크
- RESTful API 구축하는 데에 도움을 줌
- 장점
    - 사용자 인증과 권한 관리를 간단히 할 수 있음
    - 편리한 API 개발 가능

<br>
 
## DRF 사용해보기
1. 설치
    ```
    $ pip install djangorestframework
    ```

<br>

2. models.py 작성
    ```python
    from django.db import models

    # Create your models here.
    class TODO(models.Model):
        title = models.CharField(max_length=200)
        completed = models.BooleanField()
    ```

<br>

3. serializers.py 작성
    ```python
    from rest_framework import serilalizers
    from .models import TODO

    class TODOSerializer(serilalizers.ModelSerializer):
        class Meta:
            model = TODO
            fields = "__all__"
    ```

<br>

4. veiws.py
    ```python
    from django.shortcuts import render
    from .models import TODO
    from .serializers import TODOSerializer
    from rest_framework import viewsets

    class TODOViewSet(viewsets.ModelViewSet):
        queryset = TODO.objects.all()
        serializer_class = TODOSerializer()
    ```

<br>

5. app/urls.py 작성
    ```python
    from rest_framework.routers import DefaultRouter
    from .views import TODOViewSet

    router = DefaultRouter()
    router.register("TODO", TODOViewSet)

    # 추가시 urlpatterns = router.urls
    urlpatterns = router.urls
    ```

6. proejct/urls.py 작성
    ```python
    urlpatterns = [
        path("admin/", admin.site.urls), 
        path("api/", include("drf_test.urls")),
    ]
    ```