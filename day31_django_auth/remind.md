# 복습

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

## 안전영역
- 전체 물의 높이의 범위를 for문으로 돌면서 해당 높이보다 작은 높이의 영역이 나오면 그래프 알고리즘을 사용하여 연결된 영역을 찾아줍니다.