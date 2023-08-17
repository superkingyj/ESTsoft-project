import sys

N = int(sys.stdin.readline())
DP = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    input = list(map(int, sys.stdin.readline().split()))
    for j in range(1, i + 1):
        DP[i][j] = input[j - 1]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - 1]) + DP[i][j]

print(max(DP[-1]))
