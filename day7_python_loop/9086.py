import sys

T = int(sys.stdin.readline())

for _ in range(T):
    input = sys.stdin.readline().rstrip()
    print(f"{input[0]}{input[-1]}")

