import sys

x, y = map(int, sys.stdin.readline().split())
date = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31, 4: 30, 6: 30, 9: 30, 11: 30, 2: 28}
day = {1: "MON", 2: "TUE", 3: "WED", 4: "THU", 5: "FRI", 6: "SAT", 0: "SUN"}

for i in range(1, x):
    y += date[i]

print(day[y % 7])
