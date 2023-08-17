import sys

N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
cnt = 0

for coin in coins[::-1]:
    if coin > K:
        continue

    cnt += K // coin
    K %= coin

print(cnt)
