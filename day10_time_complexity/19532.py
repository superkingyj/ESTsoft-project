import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())
x, y = 0, 0
flag = False

for x_cand in range(-999, 1000):
    for y_cand in range(-999, 1000):
        if a*x_cand + b*y_cand == c and d*x_cand + e*y_cand == f:
            x, y = x_cand, y_cand
            flag = True
            break
    
    if flag: break

print(x, y)