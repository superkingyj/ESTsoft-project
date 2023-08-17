import sys

N = int(sys.stdin.readline())
left_space = N-1
middle_space = -1

for i in range(1, N+1):
    if i == N: print("*" * (N*2-1))
    elif i == 1: print(" " * left_space + "*")
    else: print(" " * left_space + "*" + " " * middle_space + "*")
    left_space -=1 
    middle_space += 2