import sys
from collections import defaultdict

N = int(sys.stdin.readline())
nums_dict = defaultdict(int)

for num in list(map(int, sys.stdin.readline().split())):
    nums_dict[num] += 1

M = int(sys.stdin.readline())
for target in list(map(int, sys.stdin.readline().split())):
    print(nums_dict[target], end=" ")
