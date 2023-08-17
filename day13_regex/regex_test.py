import re

# pattern = r"apple"
# string = "I have an apple and ad orange"

# result = re.search(pattern, string)
# print(result)


# []: 대괄호 내에 있는 문자들 중 하나와 매치
# pattern = r"a[bcd]*d"
# string = "ab, abcd, abbcd, acd"

# result = re.findall(pattern, string)
# print(result)


# +: 바로 앞 문자가 1개 이상 있으면 일치
# pattern = r"ab+c"
# string = "ac, abc, abbc, abbbc, abdc"

# result = re.findall(pattern, string)
# print(result) ['abc', 'abbc', 'abbbc']


# *: 바로 앞 문자가 0개 이상 있으면 일치
# pattern = r"ab*c"
# string = "ac, abc, abbc, abbbc, abdc"

# result = re.findall(pattern, string)
# print(result)


#
# pattern = r"(ab)+"
# string = "abc, ababc, abababc, ab, aabbc"

# result = re.findall(pattern, string)
# print(result)


# pattern = r"[aeiou]"
# string = "apple, orange, banana"

# result = re.findall(pattern, string)
# print(result)


# [?-?]: 범위 안의 요소 중 하나와 매치
# pattern = r"[0-9]"
# string = "1234567890"

# result = re.findall(pattern, string)
# print(result)


# pattern = r"\d"
# string = "I have 10 apples and 5 bananas"

# result = re.findall(pattern, string)
# print(result) # ['1', '0', '5']


# \d+: 숫자를 붙여서
# pattern = r"\d+"
# string = "I have 10 apples and 5 bananas"

# result = re.findall(pattern, string)
# print(result) # ['10', '5]


# \w+: 특수문자를 제외한 문자나 숫자 전부
# pattern = r"\w+"
# string = "Hello, World! 123"

# result = re.findall(pattern, string)
# print(result)  # ['10', '5]


# ^: 캐럿. 시작점부터 체크
# pattern = r"^Hello, W"
# string = "Hello, World!, Hello Python"

# result = re.findall(pattern, string)
# print(result)


# $: 끝부분부터 체크
# pattern = r"Python$"
# string = "Hello, World!, Hello Python"

# result = re.findall(pattern, string)
# print(result)


# {?, ?}: 바로 앞 문자 반복 범위 지저
# pattern = r"a{1,3}"
# string = "ab, abc, aabc, aaabc"

# result = re.findall(pattern, string)
# print(result) #['a', 'a', 'aa', 'aaa']

# |: 또는
# pattern = r"a|b"
# string = "ab, abc, aabc, aaabc"

# result = re.findall(pattern, string)
# print(result)  # ['a', 'b', 'a', 'b', 'a', 'a', 'b', 'a', 'a', 'a', 'b']


# (): 그룹으로 묶기
# pattern = r"(ab)"
# string = "ababc"

# match_result = re.match(pattern, string)
# findall_result = re.findall(pattern, string)
# print(match_result)  # <re.Match object; span=(0, 2), match='ab'>
# print(match_result.group()) # ab
# print(findall_result)  # ['ab', 'ab']


# sub: replace()랑 같음
string = "문장 속에는 다양한 URL이 있습니다. https://www.example.com/, http://subdomain.example.co.kr/, www.google.com, ftp://fileserver.example.org, 이렇게 다양한 형식의 URL이 있습니다."
pattern = r"[a-z0-9.:/-]+[0-9a-z.]+[a-z./]+"

result = re.sub(pattern, "", string)
print(result)
