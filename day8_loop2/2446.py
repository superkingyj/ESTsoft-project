import sys

N = int(sys.stdin.readline())
total_star = 2*N-1
curr_star = 2*N-1

for i in range(N):
    left_space = (total_star-curr_star) // 2
    print(" " * left_space + "*" * curr_star)
    curr_star -= 2

curr_star += 4 

for i in range(1, N):
    left_space = (total_star-curr_star) // 2
    print(" " * left_space + "*" * curr_star)
    curr_star += 2