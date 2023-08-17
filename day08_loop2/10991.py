import sys

N = int(sys.stdin.readline())
left_space = N-1

for i in range(1, N+1):
    print(" " * left_space + "* " * i)
    left_space -= 1