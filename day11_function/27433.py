import sys

N = int(sys.stdin.readline())

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

print(factorial(N))