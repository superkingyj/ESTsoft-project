import sys

N = int(sys.stdin.readline())
left_space, middle_space = 0, -1

for i in range(N-1, -1, -1):
    left_space = i
    
    if i == N-1: print(" " * left_space + "*")
    else: print(" " * left_space + "*" + " " * middle_space + "*")

    middle_space += 2