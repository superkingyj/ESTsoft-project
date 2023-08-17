import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):
    encrypted = sys.stdin.readline().rstrip()
    N = int(math.sqrt(len(encrypted)))
    grid = []
    start = 0

    for i in range(N):
        grid.append(encrypted[start : start + N])
        start += N

    new_grid = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_grid[N - j - 1][i] = grid[i][j]

    for i in range(N):
        for j in range(N):
            print(new_grid[i][j], end="")
    print()
