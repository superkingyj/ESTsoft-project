from bisect import bisect_left
import sys

N = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
LIS_LENGTH = [-sys.maxsize]
LIS_VAL = []

for idx in range(1, N + 1):
    

print(len(DP))
print(*DP)
