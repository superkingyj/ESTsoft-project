from functools import reduce

# number = [1,2,3,4,5]ㅋ
# sum = reduce(lambda x, y:x+y, number)
# print(sum)


target = ["letter", "bigger"]
target_upper = list(map(lambda x:x.upper(), target))
print(target_upper)