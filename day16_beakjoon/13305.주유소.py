import sys

N = int(sys.stdin.readline())
roads = list(map(int, sys.stdin.readline().split()))
gas_stations = list(map(int, sys.stdin.readline().split()))

# 가장 작은 가격
min_val = min(gas_stations[1:N])

