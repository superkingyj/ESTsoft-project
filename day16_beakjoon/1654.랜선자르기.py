import sys

K, N = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(K)]
result = -1


def count(mid):
    cnt = 0
    for i in range(K):
        cnt += arr[i] // mid
    return cnt


def binary_search():
    global result
    left, right = 1, max(arr)

    while left <= right:
        mid = (left + right) // 2
        if count(mid) >= N:
            result = max(mid, result)
            left = mid + 1
        else:
            right = mid - 1


binary_search()
print(result)
