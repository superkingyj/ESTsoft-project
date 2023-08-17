# Django

- 목차
- [Python 가상환경을 사용하는 두 가지 도구](#python-가상환경을-생성하는-두-가지-도구)
- [Conda vs Anaconda](#conda-vs-anaconda)
- [venv로 장고 실행하기](#venv로-장고-실행하기)
- [가상환경이란?](#가상환경이란)
- [디자인 패턴](#디자인-패턴)
- [소프트웨어 아키텍처 패턴](#소프트웨어-아키텍처-패턴)
- [Django 아키텍처](#django-아키텍처)
    - [MVC 디자인 패턴](#mvc-디자인-패턴)
    - [MVT 모델](#mvt-모델)
- [MVC 패턴을 적용하기 어려운 경우](#mvc-패턴을-적용하기-어려운-상황)
- [장고 프로젝트 만들기](#장고-프로젝트-만들기)
- [settings.py](#settingspy)
- [manage.py](#managepy)
- [urls.py](#urlspy)

<br>

## Python 가상환경을 생성하는 두 가지 도구
1. conda
2. venv

<br>

## Conda vs Anaconda
- Anaconda: 패키지 관리자
- Conda: Anaconda 내에 포함된 뱀들중 하나인 가상환경 생성 도구

<br>

## venv로 장고 실행하기
![](https://velog.velcdn.com/images/superkingyj/post/e029b1a1-ae01-4e0d-9efa-d9acc8385dba/image.png)
```
$ python -m venv django_env
$ source django_env/bin/activate
```

<br>

## 가상환경이란?
- 현재 사용하고 있는 환경과 분리되는 일종의 미니 pc 환경
- 가상환경을 사용하는 이유
    1. 환경을 분리하여 필요한 프레임 워크만 가볍게 사용하여 성능을 높이기 위해
    2. 환경을 분리하여 다른 프레임워크과 버전이 충돌하는 것을 방지하기 위해
    2. 배포 시 최적화된 환경을 제공하기 위해

<br>

## 디자인 패턴
- 소프트웨어 디자인 과정에서 자주 발생하는 문제들에 대한 전형적인 해결책
- 코드에서 반복되는 디자인 문제들을 해결하기 위해 맞춤화할 수 있는 미리 만들어진 청사진
- 디자인 패턴 장점
    - 일관성 향상
    - 개발시간 단축
    - 시스템 구조 이해가 쉬워서 유지보수가 쉬움
    - 의사소통이 간편해짐
    - 검증된 구조라서 안정적인 개발 가능

<br>

## 소프트웨어 아키텍처 패턴
- 소프트웨어 개발시에 시스템을 구조화하고 조직화 하기위해서 사용되는 패턴
- **시스템의 구성요소와 각 구성요소간의 관계 정의**
- 시스템의 설계와 개발을 돕는 원칙 제공
- 클라이언트-서버 패턴
    - 시스템을 클라이언트와 서버로 나누어 각각이 분리된 역할을 수행함
    - n개의 클라이언트는 사용자 인터페이스와 관련된 역할을 수행
    - 서버는 데이터 저장과 처리를 담당함.
- 레이어드 패턴
    - 프레젠테이션 레이어 - 웹UI에 해당, api의 엔드포인트
    - 비지니스 레이어 - 실제 시스템 돌아가게 하는 로직 구현
    - 퍼시스턴스 레이어 - DB와 관련된 로직구현
    - 3가지 레이어가 순서대로 쌓여있어서 서로 의존하고 시스템을 구성함
- 싱글턴 패턴
    - 한 객체가 한 인스턴스만을 가지도록 하는 패턴
- 마이크로서비스 패턴
    - 시스템을 서비스 단위로 작게 분리하고 각 서비스를 독립적으로 배포하고 운영할 수 있게함
    - 확장성과 유연성이 좋음

<br>

## Django 아키텍처
![](https://velog.velcdn.com/images/superkingyj/post/a011a42a-67aa-4579-bf18-e6916126c75e/image.png)
- Django도 MVC 디자인 패턴을 차용함
- 그러나 약간의 차이가 있음

<br>

### MVC 디자인 패턴
- 프론트와 백을 모두 하는 소프트웨어를 만들기 위한 패턴
- Model
    - 데이터와 관련된 부분
    - 데이터베이스에서 데이터를 가져오거나 저장함
- View
    - 사용자 인터페이스와 관련된 부분
    - 사용자의 입력을 받아 컨트롤러에 전달
- Controller
    - Model과 View의 상호작용을 제어

<br>

### MVT 모델
- Model
    - 데이터와 관련된 부분
    - 데이터베이스에서 데이터를 가져오거나 저장함
- **View(Controller)**
    - Model과 View의 상호작용을 제어
- **Template(View)**
    - 사용자 인터페이스와 관련된 부분
    - 사용자의 입력을 받아 컨트롤러에 전달

<br>

## MVC 패턴을 적용하기 어려운 상황
- 간단한 스크립트나 작은 프로젝트
    - 패턴이 필요 없을 정도로 작은 프로젝트
- 복잡한 비즈니스 로직
    - 프로젝트의 비즈니스 로직이 너무 복잡한 경우
- 데이터 중심 프로젝트
    - 프로젝트가 데이터 처리에 초점을 맞춘 경우
- 프로젝트의 특수한 요구사항

<br>

## 장고 프로젝트 만들기
- 장고 설치 : pip install django
= 프로젝트 생성 : django-admin startproject projectname
- 프로젝트 폴더 이동 : cd projectname
- python manage.py migrate
- python manage.py runserver
- python manage.py startapp main
- main 아래 templates 폴더 생성
- templates 아래 main 폴더 생성
- templates 아래 main 아래 index.html 생성
- index.html <body> 에 내용 추가
- 앱 폴더 views.py에 아래 추가
   ```python
    def index(request):
        return render(request, "main/index.html")
   ``` 
- 앱 폴더 urls.py에 아래 추가
    ```python
    urlpatterns = [
        path('', views.index, name="index"),
    ]
    ```
- 프로젝트 폴더 urls.py 아래 내용 추가
    ```python
    from django.urls import path, include
    
    urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    ]
    ```

## manage.py
- db마이그레이션이나 서버실행등을 관리 파일

<br>

## settings.py
- 프로젝트의 설정을 정의하는 파일
- 데이터베이스 설정, 앱 설정, 보안 설정 담당

<br>

## urls.py
- 클라이언트 요청에 따라 적절한 뷰로 연결해줌

<br>

> MVC랑 MTV 가장 큰 차이점
> MVC: 컨트롤러 부분에 제어 관련 부분을 직접 작성 해야 함 
> MTV: 프레임워크딴에서 자체적으로 처리

> MVC는 동작 요청이 들어오면 컨트롤러가 호출되서 컨트롤러가 모델기반 뷰를 불러오는데, MVT는 HTTP에서 요청이 들어오면 모델에서 쿼리 자체를 실행해서 바로 보여주는 방식 

> MVC: v -> c -> m -> v 

> MVT: v -> m (->) v -> t