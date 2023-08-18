## 20230817_Django_4_db테이블을 생성하고 넣은 데이터를 html에 출력해보기

아래 진행 전에 가상환경 > 프로젝트~ 앱 생성해주기!(어제까지 했던 내용들)

## 데이터 베이스 테이블을 정의하기 위해서는?

- `앱이름/models.py` 파일에서 데이터베이스 테이블을 정의하기 위한 클래스(모델)를 만듭니다.

  - 예를들어

  ```py
  from django.db import models
  
  # Create your models here.
  class Post(models.Model):
      title = models.CharField(max_length=200)
      content = models.TextField()
      published_date = models.DateTimeField()
  ```

  - 이렇게 만들었는데, 그랬을 때 테이블명은?
    - 기본적으로 장고는 모델 클래스의 이름을 소문자로 변환하여 테이블 이름을 생성함
    - 따라서 `Post`라는 클래스가 있을 경우, 기본적으로 생성되는 테이블의 이름은 `post`
  - 그리고 앱 이름이 `blog`라고 한다면, 장고는 이를 고려해 실제 데이터베이스 테이블 이름을 앱이름_모델의클래스이름 형식으로 자동으로 생성
  - 따라서 `blog_post`라는 이름으로 테이블이 생성됨

- 이렇게모델만 정의 해주면 테이블이 생성이 끝나나요?

- db 마이그레이션

  - ```
    python manage.py makemigrations
    python manage.py migrate
    ```

    db에 테이블을 생성!

  

- 넣은 데이터를 처리하기 위해서는?

  - views.py파일에 데이터를 처리하는 함수를 정의함

    - 모델에서 만든 클래스 연결은?

      - import를 통해서 Post클래스 가져옴
      - 그리고 

      ``` py
      from .models import Post  
      
      # HTTP 요청(request)을 매개변수로 받고, HTTP 응답을 반환
      def read_Post_data(request):  
      
          # Post 모델의 objects 매니저를 사용하여 데이터베이스에서 모든 Post 객체를 검색함
          # 이 결과는 QuerySet이라는 객체 형태로 반환됨
          posts = Post.objects.all()  
      
          # render 함수를 호출하여, "board/index.html" 템플릿 파일을 렌더링함
          # 첫 번째 인자는 request 객체
          # 두 번째 인자는 사용할 템플릿의 경로
          # 세 번째 인자는 템플릿에서 사용할 데이터
          # 여기서는 "posts"라는 키로 Post 객체의 QuerySet을 템플릿에 전달함
          return render(request, "board/index.html", {"posts": posts})  
      
      ```

- 그럼 이 함수에 들어와야하는 request인자는 어떻게 받아오나??

  - 우리는 index페이지에 들어왔을 때에 해당 데이터를 보려고 하는 것이기 떄문에

  - index의 path가 정의되어있는 urls.py에서 연결할 뷰함수를 지정해줌

    ```
    urlpatterns = [
        path('', views.read_Post_data, name='index')
    ]
    ```

  - 페이지 접속을 하면 연결된 뷰 함수가 실행되는 것!

- 뷰에서 전달받은 데이터를 html에 넣어줌

  - 데이터를 동적으로 받아서 사용하기 위해 뭘 사용할까? => dtl

  - ```html
        <ul>
          {% for post in posts %}
          <li>
            <h2>{{post.title}}</h2>
            <p>{{post.content}}</p>
            <p>생성된 날짜: {{post.published_date}}</p>
          </li>
          {{post}} {% endfor %}
        </ul>
    ```

    