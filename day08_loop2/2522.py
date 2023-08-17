import sys

N = int(sys.stdin.readline())
star_cnt = 1
w = 1

for i in range(1, 2*N):
    left_space = N-star_cnt
    print(" " * left_space + "*" * star_cnt)

    if i == N:
        w = -1
    
    star_cnt += w