import sys

N = int(sys.stdin.readline())
total_star = 2*N
curr_star = 1
w = 1

for i in range(2*N-1):
    middle_space = total_star - (2*curr_star)
    print("*" * curr_star + " " * middle_space + "*" * curr_star)
    
    if i == N-1: 
        w = -1
    
    curr_star += w