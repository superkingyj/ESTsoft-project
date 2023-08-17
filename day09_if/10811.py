import sys

N, M = map(int, sys.stdin.readline().split())
nums = [i for i in range(1, N+1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    start -= 1
    end -= 1

    for i in range(start, (start+end)//2+1):
        left, right = i, start+end-i
        nums[left], nums[right] = nums[right], nums[left]

    # 이것도 가능
    # nums[start:end+1] = nums[start:end+1][::-1]

print(*nums)

