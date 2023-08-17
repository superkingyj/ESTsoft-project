import sys

N = int(sys.stdin.readline())
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))
curr_end = 0
cnt = 0

for start, end in arr:
    if start >= curr_end:
        cnt += 1
        curr_end = end

print(cnt)
