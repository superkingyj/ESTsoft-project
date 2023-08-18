# view
- 목록
- [데이터베이스](#데이터베이스)
- [MVT 모델의 역할](#mvt-모델의-역할)
- [django 데이터베이스 설정](#django-데이터베이스-설정)
- [setting.py 살펴보기](#settingspy-살펴보기)
- [model 만들기 실습](#model-만들기-실습)
- [view에 데이터 띄우기 실습](#view에-데이터-띄우기-실습)
- [원하는 데이터만 출력](#원하는-데이터만-출력)
- [사용자 데이터 입력 받기 실습](#사용자-데이터-입력-받기-실습)
- [사용자 입력을 어떻게 데이터베이스에 저장할까?](#사용자-입력을-어떻게-데이터베이스에-저장할까)

<br>

## 데이터베이스
- 데이터를 **구조적**으로 저장하는 공간
- 데이터를 저장할 때 colum과 row를 기준으로 저장함
- CRUD 기능 제공

<br>

## MVT 모델의 역할
- M: 데이터관리
- T: DTL, html
- View: 사용자 ~ 및 데이터 CRUD 작업
    - view 함수의 매개변수의 역할
    - 클라이언트의 HTTP 요청 정보를 받아와서 해당 요청을 처리
    - 데이터를 가공하여 응답을 생성하는 데 사용됨
    - 다양한 정보와 기능을 제공하여 뷰 함수가 원활하게 작동할 수 있도록 도와줌.

<br>

## django 데이터베이스 설정
```
$ pip install django 
$ django-admin startproject myproject 
$ python manage.py startapp board
$ python manage.py migrate # 최초 실행이므로 데이터베이스 초기 생성
```

<br>

## settings.py 살펴보기
![](https://velog.velcdn.com/images/superkingyj/post/9548eec6-1fe1-408e-92e3-b36dc74c4da9/image.png)
- settings.py에 DB 엔진(sqlite3)과 경로 관련 정보가 있음
- settings.py를 통해 DB 관련 설정을 변경할 수 있음

<br>

## model 만들기 실습
```python
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)  # Char 필드: 글자형 데이터
    content = models.TextField()  # Text 필드
    published_date = models.DateTimeField()
```
```
$ python manage.py makemigrations # 마이그레이션을 할 준비
$ python manage.py migrate # model 코드를 데이터베이스로 마이그레이션
```

<br>

## view에 데이터 띄우기 실습
- model.py
    ```python
    class Post(models.Model):
        title = models.CharField(max_length=200)  # Char 필드: 글자형 데이터
        content = models.TextField()  # Text 필드
        published_date = models.DateTimeField()

    ```
- views.py
    ```python
    from .models import Post

    def read_Post_data(request):
        posts = Post.objects.all()
        return render(request, "board/index.html", {"posts": posts})
    ```
- 프로젝트 폴더/urls.py
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", include("board.urls")), # 추가
    ] 
    ```
- 앱 폴더/urls.py
    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path("", views.read_Post_data, name="index"),
    ]
    ```
- templates/board/index.html
    ```html
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <table border='1'>
                <th>id</th> <th>title</th> <th>content</th> <th>post.published_date</th>
                {% for post in posts%}
                    <tr>
                        <td> {{ forloop.counter0 }} </td>
                        <td> {{ post.title }}  </td>
                        <td> {{ post.content }} </td>    
                        <td> {{ post.published_date|date:"Y-m-d D A h:i" }} </td>
                    </tr>
                {% endfor %}
            </table>
        </body>
    </html>
    ```

<br>

## 원하는 데이터만 출력
- title에 오르미가 들어가는 것만 출력
    ```python
    # Create your views here.
    posts = Post.objects.filter(title__contains="오르미")
    ```
- 날짜 범위 내의 데이터만 출력
    ```python
    posts = Post.objects.filter(published_date__range=(start_date, today))
    ```
<br>

## 사용자 데이터 입력 받기 실습
- add_page.html
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <form>
            <label>제목: </label>
            <input type="text" name="title" required><br>
            
            <label>내용: </label>
            <textarea type="text" name="content" rows="4" required></textarea> <br>
            
            <label>날짜: </label>
            <input type="date" name="published_date" required> <br>
            
            <input type="submit" value="Add Post">
        </form>
    </body>
    </html>
    ```
- urls.py
    ```python
    urlpatterns = [
        ...
        path("add_page", views.add_Post_data, name="add_data"),
    ]
    ```
- views.py
    ```python
    def add_Post_data(request):
        if request.method == "POST":
            title = request.POST["title"]
            content = request.POST["content"]
            published_date = request.POST["published_date"]

            post = Post(title=title, content=content, published_date=published_date)
            post.save()
            return redirect("index")

        return render(request, "board/add_page.html")
    ```

<br>

## csrf 설정
- {% csrf_token %}
- form으로 전송한 데이터가 실제 웹 페이지에서 작성한 데이터인지를 판단하는 가늠자 역할
- 만약 어떤 해커가 이상한 방법으로 데이터를 전송할 경우에는 서버에서 발행한 csrf_token 값과 해커가 일방적으로 보낸 csrf_token 값이 일치하지 않기 때문에 블록킹될 것

<br>

## 사용자 입력을 어떻게 데이터베이스에 저장할까?
1. form 제출
2. add_post 페이지에서 반응
3. **view**에 있는 함수가 실행 <- 즉 v에서 데이터 저장
4. POST 요청 / POST가 아닌 요청
5.1 POST 요청이면 데이터베이스에 추가 후 redirect('index') 해줌
5.2 POST가 아닌 요청은 add_page.html 렌더링