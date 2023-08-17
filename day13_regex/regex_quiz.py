import re

# 문제1 - 전화번호 추출
# string1 = "안녕하세요. 저의 전화번호는 !-010-1234-5678-!입니다. 다른 전화번호는 !-02-987-6543-!입니다. 지역번호가 555542-10-1"
# pattern = r"\d{2,3}-\d{3,4}-\d{4}"

# result = re.findall(pattern, string1)
# print(result)


# 문제2 -
# string1 = "안녕하세요. 이메일 주소는 abc@example.com입니다. 다른 이메일은 def@hcu.co.kr이고, x_yz@hotmail.net 있습니다."
# pattern = r"[.+@\w+[.a-z]+"

# result = re.findall(pattern, string1)
# print(result)


# 문제3 - URL 찾기
string1 = "문장 속에는 다양한 URL이 있습니다. https://www.example.com/, http://subdomain.example.co.kr/, www.google.com, ftp://fileserver.example.org, 이렇게 다양한 형식의 URL이 있습니다."
pattern = r"[\w:/]+[0-9\w.]+[0-9a-z/]+"

result = re.findall(pattern, string1)
print(result)
