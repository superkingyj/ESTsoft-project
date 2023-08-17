import sys
from itertools import combinations

nums = [int(sys.stdin.readline()) for _ in range(9)]
combis = combinations(nums, 7)
result = []

for combi in combis:
    if sum(combi) == 100:
        result = list(combi)
        break

result.sort()
for num in result:
    print(num)
