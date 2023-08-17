import sys

N = int(sys.stdin.readline())

total_space = 2 * N
star_cnt = 1

for i in range(N):
    left_space = (total_space-star_cnt) // 2
    print(" "*left_space + "*" * star_cnt)
    star_cnt += 2

total_space = 2*N-1
star_cnt = 2*N-3

for i in range(1, N):
    left_space = (total_space-star_cnt) // 2
    print(" "*left_space + "*" * star_cnt)
    star_cnt -= 2