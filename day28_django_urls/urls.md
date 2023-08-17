# URLS
- 목차
- [views.py](#viewspy)
- [urls.py](#urlspy)

<br>

## views.py
```python
def index(request):
    return render(request, "main/index.html")

def new_page(request):
    return render(request, 'main/oreumi_page.html')

def new_page2(request):
    return render(request, 'main/oreumi_page2.html')
```
- 해당 html 템플릿을 렌더링 해서 보여줌

<br>

## urls.py
```python
urlpatterns = [
    path("", views.index, name="index"),
    path("oreumi", views.new_page, name="page"),
    path("oreumi2", views.new_page2, name="page2"),
]
```
- 프로젝트 폴더의 url
    - 최상위 url패턴을 정의
    - 각 앱들의 url설정과 연결
- 앱 폴더의 url
    - 앱 레벨 url 패턴을 정의
- urlpatterns
    - URL 경로를 뷰에 연결
- path
    - 뷰를 연결 / 이름 할당 / 동적으로 뷰함수에 인자 전달
    - path의 첫번째 인자
        - URL 패턴 매핑
        - oreumi, oreumi2
    - path의 두번째 인자
        - 해당 URL 패턴에 매칭되는 뷰
        - views.new_page, views.new_page2
    - path의 세번째 인자
        - html에서 DTL로 사용될 이름
<br>

## url 매핑 방법
- 정규표현식 사용
- url 매개변수 사용
    - urls.py
    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('problem/<int:problem_id>', views.problem, name='page2'),
    ]
    ```

    - views.py
    ```python
    def problem(request):
        return render(request, 'problem/{}.html'.format(request.problem_id))
    ```
- includ 함수 사용
    ![](https://velog.velcdn.com/images/superkingyj/post/b855b6f4-6bc5-4d07-8beb-0cf587c3e561/image.png)
    - 다른 url 설정 파일을 참조할 떄 사용
    - 장점
        1. URL 파일구조 분리
        2. 공통경로 부여(접두사 사용)
    - include('blog.urls')부분에서 blog.urls 모듈에서 정의한 url패턴들을 가져오게 됨
    - 가져온 url패턴들에 접두사를 'blog/'라고 붙여주어서 메인 urls.py에 추가

<br>

## DTL
- Django 템플릿 언어
- Django 템플릿에서 동적인 내용을 표시할 수 있음
- DTL을 사용하여 view에서 보내주는 데이터를 쓸 수 있음
- 변수 표시
    ```
    {{ title }}
    ```
    - 중괄호 두개 안에 변수를 넣음
- 반복문
    ```
    { % for item in items %}
        <li> {{ item }} </li>
    { %endfor %}
    ```
- 조건문
    ```
    {% if is_authenticated %}
        <p> welcome </p>
    { % else %}
        <p>please log in</p>
    { % endf %}
    ```
- 필터
    ```
    <p> {{ price|currency }} </p>
    ```
    - 데이터를 변환하거나 형식을 지정함
    - 파이프|를 사용하여 적용


<br>

## redirect
- 뷰 함수에서 redirect라는 함수 이용
- urls.py에서 RedirectView를 임포트해와서 사용
    ```python
    path('original_url/', RedirectView.as_view(url='/other_url')),
    ```
    1. RedirectView를 임포트
    2. path에서 RedirectView.as_view() 메서드를 사용해서 url변수에 리디렉션 목적지의 url을 지정
- 내장 앱을 settings.py에 추가해서 사용