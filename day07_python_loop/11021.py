import sys

T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(f"Case #{i+1}: {A+B}")
