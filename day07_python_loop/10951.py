import sys

lines = sys.stdin.readlines()

for line in lines:
    print(sum(map(int, line.split())))