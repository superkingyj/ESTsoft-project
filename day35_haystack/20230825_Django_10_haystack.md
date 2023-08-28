# haystack 라이브러리 이용해서 간단하게 검색기능 구현하기'

---

- haystack은 검색엔진 플랫폼같은 느낌
- Haystack을 사용하면 Django 애플리케이션에서 쉽게 검색 엔진을 통합하고 복잡한 검색 기능을 구현할 수 있음
- 예를들어서 엘라스틱서치, Solr, Whoosh등이 있는데 
  - 엘사
    - 실시간 분산 검색 및 분석 엔진으로, 대량의 데이터를 빠르게 검색하고 분석할 수 있는 오픈 소스 솔루션
    - 대용량 데이터를 처리하며 확장성이 뛰어남 
    - RESTful API를 통해 데이터에 접근할 수 있음 
    - 특히 로그 분석이나 대규모 데이터 검색에 많이 사용됨.
  - Solr
    - 검색엔진
    - 아파치를 기반으로 구축된 오픈소스 솔루션
    - XML/Json/HTTPㄷ등 다양한 데이터 입력 지원
    - 엘사와 유사하게 사용됨. 마찬가지로 대용량 데이터 처리에 적합
  - Whoosh
    - 오픈소스 텍스트 검색 라이브러리
    - 작은 규모의 프로젝트나 단순한 검색에 적합
    - 위 보다는 성능이나 기능 제한적이지만 훨씬 가볍고 pc에 직접 설치할 필요 x

---

**단계 1: 프로젝트 및 앱 설정**

1. 가상환경 실행+ 프로젝트와 앱 만들기

```bash
django-admin startproject search_example # 프로젝트 생성
cd search_example # 프로젝트로 이동
python manage.py startapp myapp # 프로젝트 내 앱 생성
```

2. haystack + 연결할 검색라이브러리인 Whoosh 설치

   ```bash
   pip install django-haystack
   pip install Whoosh
   ```

   * 헤이스탁 설치시 오류나면
     search_example(프로젝트)경로에 requirements.txt생성하고 아래처럼 입력

     ```
     Django==3.2.6
     django-haystack==3.0
     ```

     그리고 명령어 입력으로 해당 프로그램들 설치
     ```
     pip install -r requirements.txt
     ```

     

2. `settings.py` 파일에 설치한 앱 추가

```python
INSTALLED_APPS = [
    # ...
    'haystack',
    'myapp',
    # ...
]

```

3. 데이터베이스 처리

```bash
python manage.py migrate
```

**단계 2: 모델 생성**

1. `myapp/models.py` 파일에 간단한 모델을 생성함

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title
```

2. 모델 변경 사항을 반영

```bash
python manage.py makemigrations myapp
python manage.py migrate
```

**단계 3: Haystack 설정**

1. `myapp/search_indexes.py` 파일을 생성함

```python
from haystack import indexes
from .models import Book

class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)

    def get_model(self):
        return Book

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

```

2. 앱에 `templates` 디렉토리를 생성하고 
   그 안에 `templates/search/indexes/myapp/book_text.txt` 파일을 생성함

```txt
{{ object.title }}
{{ object.content }}
```

3. `settings.py` 파일에 헤이스탁설정을 추가

```python
import os
...
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
```

**단계 4: 검색 뷰 생성**

1. `myapp/views.py` 파일에 검색 뷰를 생성

```python
from django.shortcuts import render
from haystack.query import SearchQuerySet

def search_view(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = SearchQuerySet().filter(text=query)

    context = {'results': results}
    return render(request, 'myapp/search_results.html', context)
```

2. `myapp/templates/myapp` 디렉토리를 생성하고 그 안에 `base.html`파일과 `search_results.html` 파일을 생성

   - base.html

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>{% block title %}My Website{% endblock %}</title>
     </head>
     <body>
       <header>
         <h1>도서검색</h1>
         <nav>
           <a href="{% url 'search_view' %}">다시 검색하기</a>
         </nav>
       </header>
       <main>{% block content %}{% endblock %}</main>
       <footer>
         <p>&copy; 2023 yewonlee</p>
       </footer>
     </body>
   </html>
   
   ```

   - search_results.html

```html
{% extends "./base.html" %} {% block content %}
<form method="GET" action="{% url 'search_view' %}">
  <input type="text" name="q" placeholder="제목 혹은 저자 키워드" />
  <button type="submit">Search</button>
</form>

<ul>
  {% for result in results %}
  <li>{{ result.object.title }}</li>
  {% endfor %}
</ul>
{% endblock %}

```

**단계 5: URL 설정**

1. `myapp/urls.py` 파일에 검색 뷰를 위한 URL을 추가

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_view, name='search_view'),
]

```

2. 프로젝트 레벨의 urls.py파일에 myapp의 url연결

   ```py
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('myapp.urls')),
   ]
   ```

---

### 관리자 페이지에서 데이터 추가

- myapp/admin.py 에 모델 등록

```
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

- 슈퍼유저 생성

  ```
  python manage.py createsuperuser
  ```

- 서버 실행 후 http://127.0.0.1:8000/admin/에 접속해서 데이터 추가!

---

### 데이터 인덱싱

- 헤이스탁은 검색엔진을 사용하기 떄문에 데이터를 인텍싱하는 것이 필요함!

- 명령어 입력(데이터 바뀔때마다 해주어야 함)

  ```
  python manage.py rebuild_index
  ```

- 끝! 서버 실행!

  ```
  python manage.py runserver 
  ```


https://startbootstrap.com/templates?showAngular=false&showVue=false&showPro=false