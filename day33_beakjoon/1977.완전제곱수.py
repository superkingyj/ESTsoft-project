import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
nums = []

for num in range(M, N + 1):
    if num**0.5 == int(num**0.5):
        nums.append(num)

if not nums:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))
