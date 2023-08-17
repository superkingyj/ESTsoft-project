import sys

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

tmp1, tmp2 = (A // C), (B // D)
if A % C:
    tmp1 += 1
if B % D:
    tmp2 += 1

print(L - max(tmp1, tmp2))
