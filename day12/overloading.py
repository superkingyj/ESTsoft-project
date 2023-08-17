# 오버라이딩: 덮어 쓰기
# 오버로딩: 동일한 이름의 서로 다른 매개변수를 가진 함수를 여러개 사용하는 것
# over loading: 여러 개를 로딩한다
# python에는 오버로드가 없고 가장 최근에 정의된 함수만 유효함

def add(a, b):
    return a+b

def add(a,b,c):
    return a+b+c

print(add(1,3))