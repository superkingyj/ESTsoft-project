import sys, re

# N = int(sys.stdin.readline())
# nums = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# target = list(map(int, sys.stdin.readline().split()))

# nums_set = set(nums)
# target_set = set(target)
# nums_and_target = nums_set.intersection(target_set)

# for num in target:
#     print(1, end=" ") if num in nums_and_target else print(0, end=" ")


"""
8글자 이상
영어 대소문자, 숫자, 특수문자를 모두 포함
공백은 포함되면 안됨
해당 조건을 모두 만족하는 정규식을 작성해주세요

"""

# string = "Dbwlscjswosla13, dbwlsdl13, Dbwlsdl19"
# pattern = r"(?=.[A-Z])(?=.[a-z])(?=.\d)(?=.[!@#$%^&()_+])[A-Za-z\d!@#$%^&()_+]{8,}"
# result = re.findall(pattern, string)
# print(result)

try:
    daily_input = oreumi.daily
except AttributeError as e:
    print("Error: ", e)


