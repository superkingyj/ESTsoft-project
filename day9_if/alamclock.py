import sys

H, M = map(int, sys.stdin.readline().split())
new_m, new_h = 0, 0 
if M < 45:
    if H == 0 : new_h = 23
    else: new_h = H-1
    new_m = M+15
else:
    new_h = H
    new_m = M-45


print(f"{new_h} {new_m}")
