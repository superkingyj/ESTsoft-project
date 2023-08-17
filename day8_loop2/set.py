# list -> set
numbers = [1,2,2,3,3,5]
set_numbers = set(numbers)

a = {1,2,3,5}
b = {6,7,8,5}
c = {1,2}

# 교집합 구하기
print(a.intersection(b))
print(a&b)

# 합집합 구하기
print(a.union(b))
print(a|b)

# 차집합 구하기 
print(a.difference(b))
print(a-b)

# 부분집합인지 확인
print(a.issubset(b))
print(c.issubset(a))

# 원소가 있는지 확인
print(2 in a)

# set에 쓸 수 있는 함수
a.add(4)
a.remove(4)
a.discard(4)
