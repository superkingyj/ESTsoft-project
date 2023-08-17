import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    star_str = ""
    for j in range(i):
        star_str += "*"
    print(star_str)

for i in range(1, N+1):
    print("*" * i)