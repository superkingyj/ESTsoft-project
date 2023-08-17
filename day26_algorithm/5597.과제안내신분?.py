import sys

arr = [i for i in range(1, 31)]
for _ in range(28):
    arr.remove(int(sys.stdin.readline()))

print(min(arr))
print(max(arr))
