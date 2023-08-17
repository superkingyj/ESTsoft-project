import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())
h_cnt = 0

if B+C >= 60: 
    m = (B+C) % 60
    h_cnt = (B+C) // 60
else: 
    m = B+C

h = (A+h_cnt) % 24
print(h, m)
