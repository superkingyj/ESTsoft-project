# Django 소셜로그인 적용

---

## 구글 개발자 콘솔에서 미리 설정

- 구글 개발자 콘솔 접속

  - http://console.developers.google.com/

- 프로젝트 만들기 클릭

- 프로젝트 만듦(프로젝트 이름 임의로, 소속은 없어도 됨)

- OAuth 동의 화면 클릭

  - 사용자 인증정보 만들기 클릭

  - OAuth 클라이언트 ID선택

  - 동의화면 구성

  - 외부 선택, 만들기

    - OAuth 동의화면

      - 앱이름(임의 생성)

      - 사용자 지원 이메일(본인 이메일)

    - 개발자 연락처 정보(본인 이메일)

    - 저장 후 계속

    - 범위

      - 범위 추가 또는 삭제클릭
      - email / profile / openid 선택 후 하단 업데이트 선택
      - 저장 후 계속

    - 테스트 사용자

      - ADD USERS
        - 테스트 사용자는 이메일 주소 기준으로 진행이 됨
        - 본인 지메일 추가
      - 저장 후 계속

- 사용자 인증정보 만들기

  - 사용자 인증 정보 탭 누르기
  - 사용자 인증정보 만들기 클릭
  - OAuth 클라이언트 ID선택
  - 어플리케이션 유형: 웹애플리케이션 
  - 승인된 자바스크립트 원본 / 리디렉션 URI에 주소 추가
    - 원본
      - http://127.0.0.1:8000
    - 리디렉션
      - http://127.0.0.1:8000/complete/google-oauth2/
  - 만들기 



---

## 장고 설정

   - `social-auth-app-django` 라이브러리를 설치합니다.

     ```bash
     pip install social-auth-app-django
     ```

   - 앱 설치 및 settings에 등록

   - `settings.py` 파일에 아래와 같이 구글 로그인에 관련된 설정을 추가합니다.
     (각 값은 아까 설정한 구글의 OAuth 2.0 클라이언트 ID에서 확인가능 )
     
     ```python
     INSTALLED_APPS = [
     ...
         'social_django'
     ]
     
     SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '899385276005-9oman0l6hgth4162so235ttg8jg2f3i3.apps.googleusercontent.com'
     SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
     SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'http://127.0.0.1:8000/complete/google-oauth2/'
     
     AUTHENTICATION_BACKENDS = (
         'social_core.backends.google.GoogleOAuth2',
         'django.contrib.auth.backends.ModelBackend',
     )
     ```

   - 앱의 views.py 코드 추가
     (특별히 추가적인 view 함수를 작성하지 않아도 `social-auth-app-django`가 로그인 처리를 대신 해줍니다.)
     
     ```py
     from django.shortcuts import render
     
     def login_view(request):
         return render(request, 'main/login.html')
     ```
     
     
     
   - 앱의 urls.py파일에서 URL을 설정

     ```py
     from django.urls import path
     from . import views
     
     urlpatterns = [
         path('', views.login_view, name='login'),
     ]
     ```

     

   - 프로젝트의 `urls.py` 파일에서 URL을 설정

     ```python
     from django.contrib import admin
     from django.urls import path, include
     
     urlpatterns = [
         path('admin/', admin.site.urls),
         path('', include('social_django.urls')),
         path('', include('main.urls'))
     ]
     ```

   - login.html 작성

     ```html
     <!DOCTYPE html>
     <html>
       <head>
         <title>Login</title>
       </head>
       <body>
         <h1>Login</h1>
         <a href="{% url 'social:begin' 'google-oauth2' %}">Google 로그인</a>
       </body>
     </html>
     ```

---

## 네이버 소셜로그인 추가

### 한번 로그인 된 후에는 자동으로 리디렉션 됨

- 네이버 개발자 콘솔에서 애플리케이션을 등록하고 클라이언트 ID와 시크릿 키를 받아옵니다.

  - https://developers.naver.com/apps/#/wizard/register
  - ...이후추가^^
  

---

## CSS 적용

- html파일수정

  - ```
    {% load static %}
    <!DOCTYPE html>
    <html>
      <head>
        <link
          rel="stylesheet"
          type="text/css"
          href="{% static 'css/styles.css' %}"
        />
        <title>Login</title>
      </head>
      <body>
        <div class="login-container">
          <h1>Login</h1>
          <div>
            <a
              class="login-button red"
              href="{% url 'social:begin' 'google-oauth2' %}"
              >Google 로그인</a
            >
            <a class="login-button green" href="{% url 'social:begin' 'naver' %}"
              >네이버 로그인</a
            >
          </div>
        </div>
      </body>
    </html>
    
    ```

- css추가

  - ```
    /* css/styles.css */
    
    body {
        font-family: Arial, sans-serif;
        background-color: #f2f2f2;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
      }
      
      .login-container {
        text-align: center;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
      }
      
      .login-container h1 {
        margin-bottom: 20px;
      }
      
      .login-button {
        display: inline-block;
        margin: 5px;
        padding: 10px 20px;
        font-size: 16px;
        text-align: center;
        color: white;
        background-color: #f44242;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        text-decoration: none;
        font-weight: 700;
      }
      
    .red{
        background-color: #f44242;
    
    }
    
    .green{
        background-color: #11af33;
    
    }
    
    .red:hover{
        background-color: #d13434;
    
    }
    
    .green:hover{
        background-color: #148d2e;
    
    }
    
    ```

    