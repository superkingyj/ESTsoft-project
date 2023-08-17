import sys

N = int(sys.stdin.readline())
input = sys.stdin.readline().rstrip()
sum_val = 0
for i in range(N):
    sum_val += int(input[i])

print(sum_val)