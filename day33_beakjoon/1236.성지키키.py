import sys

N, M = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
row_cnt, col_cnt = 0, 0

for i in range(N):
    if "X" not in grid[i]:
        row_cnt += 1

for j in range(M):
    if "X" not in [grid[i][j] for i in range(N)]:
        col_cnt += 1

print(max(row_cnt, col_cnt))
