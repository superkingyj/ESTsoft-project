# auth
- 목차
- [사용자 요청 흐름](#사용자-요청-흐름)
- [setting.py](#settingspy)
- [사용자 인증 방식](#사용자-인증-방식)

<br>


## 사용자 요청 흐름
1. http://www.oreumi.co.kr 을 DNS에서 주소를 받아옴
2. 브라우저가 해당 주소로 연결
3. Django 서버로 진입
4. 프로젝트 레벨 URL에서 사용자 요청 url 매칭
5. 앱 레벨 URL에서 사용자 요청 url 매칭
6. View 진입
7. Model에서 데이터 요청
8. 반환 받은 데이터로 template 렌더링
9. Django 서버가 렌더링 된 html 반환


<br>

## settings.py
- 정적 파일 설정
- 미디어 파일 설정
- 데이터베이스 설정


<br>

## 사용자 인증 방식
1. 폼 기반 인증
    - 사용자가 제출한 로그인 폼의 아이디/비번을 사용하여 인증하는 방식
2. 소셜 로그인
    - 소셜 미디어 서비스 계정을 사용하여 인증하는 방식
    - OAuth, OpenID Connect 등 프로토콜 사용
3. 다단계 인증
    - 여러 단계의 인증 절차를 거치는 것
    - ex. 비밀번호 -> sms 인증코드
4. 토큰 기반 인증

<br>

## CSRF
![](https://velog.velcdn.com/images/superkingyj/post/16c40ab0-2989-4bef-8347-90da4f713935/image.png)
- "Cross-Site Request Forgery (CSRF)
- HTML 안에 또 다른 HTML 코드를 넣어 사용자가 의도하지 않은 동작을 하도록 만드는 공격방법
1. 로그인 시에 `csrf_token`을 생성하고 사용자 세션에 저장
2. 웹 페이지를 생성할 때, 생성된 `csrf_token`을 포함시킴 
3. 사용자가 어떤 액션을 수행할 때 (예: 폼을 제출할 때), 해당 `csrf_token`을 요청과 함께 전송함
4. 서버는 수신한 `csrf_token`이 사용자 세션에 저장된 값과 일치하는지 확인
5. `csrf_token`이 일치하지 않으면 요청을 거부

<br>

## 뷰에서 사용할 수 있는 form 양식
```python
# 예시 코드
from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()
    
```

```html
{% if form.name.errors %}
    <div class="error">{{ form.name.errors }}</div>
{% endif %}

```
1. **`django.forms.Form`**: 일반적인 폼 클래스로, 여러 필드를 가질 수 있습니다. 개별 필드의 유효성 검사를 위해 `clean_필드이름()` 메서드를 사용할 수 있습니다.
2. **`django.forms.ModelForm`**: 데이터베이스 모델과 연결된 폼을 생성하는 데 사용됩니다. 모델의 필드와 연결되는 폼 필드를 자동으로 생성하며, 모델 인스턴스의 생성 및 수정을 지원합니다.
3. **`django.forms.CharField`**: 문자열 입력 필드를 나타냅니다.
4. **`django.forms.IntegerField`**: 정수 입력 필드를 나타냅니다.
5. **`django.forms.EmailField`**: 이메일 주소 입력 필드를 나타냅니다.
6. **`django.forms.URLField`**: URL 입력 필드를 나타냅니다.
7. **`django.forms.BooleanField`**: 참/거짓 선택을 위한 체크박스 필드를 나타냅니다.
8. **`django.forms.ChoiceField`**: 선택 항목 중 하나를 선택하는 드롭다운 메뉴 형태의 입력 필드를 나타냅니다.
9. **`django.forms.FileField`**: 파일 업로드를 위한 입력 필드를 나타냅니다.
10. **`django.forms.DateField`**: 날짜 입력 필드를 나타냅니다.
11. **`django.forms.TimeField`**: 시간 입력 필드를 나타냅니다.
12. **`django.forms.DateTimeField`**: 날짜와 시간 입력 필드를 나타냅니다.
13. **`django.forms.Textarea`**: 여러 줄의 텍스트 입력을 위한 입력 필드를 나타냅니다.
14. **`django.forms.PasswordInput`**: 비밀번호 입력을 위한 필드를 나타냅니다. 입력 내용은 가려져서 표시됩니다.
15. 등등...