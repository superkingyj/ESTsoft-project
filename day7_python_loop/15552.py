import sys

T = int(sys.stdin.readline())

for _ in range(T):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(num1 + num2)