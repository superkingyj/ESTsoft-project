import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
prefers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0

for num1, num2, num3 in combinations(range(M), 3):
    tmp = 0
    for i in range(N):
        tmp += max(prefers[i][num1], prefers[i][num2], prefers[i][num3])
    result = max(result, tmp)

print(result)
