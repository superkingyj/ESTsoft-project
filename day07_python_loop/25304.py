import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
sum_val = 0

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    sum_val += a*b

print("Yes") if sum_val == X else print("No")
