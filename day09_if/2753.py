import sys

year = int(sys.stdin.readline())

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0): print(1)
else: print(0)