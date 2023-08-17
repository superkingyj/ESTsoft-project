import sys

N = int(sys.stdin.readline())
DP = [0] * (N+1)

for i in range(1, N+1):
    DP[i] = DP[i-1]+i

print(DP[-1])