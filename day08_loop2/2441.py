import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    star_cnt = (N+1-i)
    print(" " * (N-star_cnt) + "*" * star_cnt)