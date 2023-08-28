# DRF이용해서 API만들고 문서화 하기



0. 가상환경 설정

   ```
   python -m venv django_env
   
   .\django_env\Scripts\activate.bat 윈도우의 경우
   source django_env/bin/activate  맥,리눅스의 경우



1. **환경 설정**:

    - Django 및 DRF 설치
      ```bash
      pip install django
      pip install djangorestframework
      ```

    - 프로젝트 생성
      ```bash
      django-admin startproject myproject
      ```

    - 앱 생성
      ```bash
      cd myproject
      python manage.py startapp products
      ```

2. **모델 생성**:
    - `products/models.py`에서 상품 모델을 정의함

      ```python
      from django.db import models

      class Product(models.Model):
          name = models.CharField(max_length=255)
          price = models.DecimalField(max_digits=10, decimal_places=2)
          description = models.TextField()

          def __str__(self):
              return self.name
      ```

    - 모델 변경사항을 데이터베이스에 반영하기 위해 마이그레이션을 생성하고 적용함

      ```bash
      python manage.py makemigrations
      python manage.py migrate
      ```

3. **DRF Serializer 생성**:
    - `products/serializers.py`에 상품에 대한 Serializer를 생성

      ```python
      from rest_framework import serializers
      from .models import Product
      
      class ProductSerializer(serializers.ModelSerializer):
          class Meta:
              model = Product
              fields = '__all__'
      ```

4. **API View 생성**:
    - `products/views.py`에서 API view를 생성

      ```python
      from rest_framework import generics
      from .models import Product
      from .serializers import ProductSerializer
      
      class ProductListCreateView(generics.ListCreateAPIView):
          queryset = Product.objects.all()
          serializer_class = ProductSerializer
      ```

5. **URL 연결**:
    - `products/urls.py`에 API endpoint를 연결

      ```python
      from django.urls import path
      from .views import ProductListCreateView

      urlpatterns = [
          path('products/', ProductListCreateView.as_view(), name='product-list-create'),
      ]
      ```

    - 프로젝트의 주요 `urls.py`에 위에서 정의한 `products/urls.py`를 연결

      ```python
      from django.contrib import admin
      from django.urls import path, include
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('api/', include('products.urls')),
      ]
      ```

6. **Swagger로 문서화**:
    - DRF-YASG (Yet Another Swagger Generator)를 설치

      ```bash
      pip install drf-yasg
      ```

    - 프로젝트의 주요 `urls.py`에 swagger와 redoc 문서화 경로를 추가

      ```python
      from rest_framework import permissions
      from drf_yasg.views import get_schema_view
      from drf_yasg import openapi
      
      schema_view = get_schema_view(
         openapi.Info(
            title="Products API",
            default_version='v1',
            description="Products API documentation",
         ),
         public=True,
         permission_classes=(permissions.AllowAny,),
      )
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('api/', include('products.urls')),
          path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
          path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
      ]
      ```

7. Settings.py 설정

    ```py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',  # DRF
        'drf_yasg', #swagger
        'products',
    ]
    
    ```

    

8. **개발 서버 실행**:

    ```bash
    python manage.py runserver
    ```

서버 실행하고 `http://127.0.0.1:8000/swagger/`로 접속하기!



# Admin계정으로 데이터 추가하기

먼저 `products` 앱의 모델을 관리자 페이지에서 사용하려면 `admin.py` 파일을 아래처럼 수정해야함
```python
from django.contrib import admin
from .models import Product

admin.site.register(Product)
```

- 관리자 페이지로 접속하려면, 먼저 superuser 계정을 생성
  ```
  python manage.py createsuperuser
  ```
  위의 명령을 실행하여 필요한 정보를 입력하면 superuser 계정이 생성

  이후, `/admin/` 경로로 접속해서 내용 추가!

  뭐 없다~ 이런 내용 에러 뜨면 db.sqlite3에 db뜨는지 한번 확인하고,
  없다면 마이그레이션 다시해줘보기!

  ```
  python manage.py makemigrations products
  python manage.py migrate products
  ```

  

