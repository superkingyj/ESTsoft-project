카카오 (카카오 소셜 id 연동 검색하면 나옴)
로그인-내 애플리케이션-애플리케이션 추가하기-
앱 이름: social_test
사업자명: oreumi

-카카오 로그인(제품 설정 밑)-활성화 설정-
Redirect URI 등록: http://127.0.0.1:8000/accounts/kakao/login/callback/

-> 동의항목(카카오 로그인 아래/ 닉네임, 필수 동의로 변경 이용목적은 아무거나)

-> 보안(코드 생성, 활성화 상태 사용함으로 변경)

-> 허용 IP주소 클릭-(https://www.findip.kr/ 사이트 들어가서 내 ip주소 복사해서 붙여넣기)

-> 플랫폼(web플랫폼 등록-http://127.0.0.1:8000)

-> 터미널: pip install django-allauth
rest api 키
보안 페이지에서 -> secret key키

client id -> rest api
secret key -> secret key 
chosen-sites +버튼 