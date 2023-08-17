import sys


N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt, num = 0, -1
answer = []


def merge_sort(arr):
    global answer, cnt, num

    if len(arr) == 1:
        return arr

    mid = (len(arr) + 1) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def check_cnt(_num):
    global cnt, num

    cnt += 1
    if cnt == K:
        num = _num


def merge(left, right):
    l, r = 0, 0
    result = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            answer.append(left[l])
            check_cnt(left[l])
            l += 1
        else:
            result.append(right[r])
            answer.append(right[r])
            check_cnt(right[r])
            r += 1

    while l < len(left):
        result.append(left[l])
        answer.append(left[l])
        check_cnt(left[l])
        l += 1

    while r < len(right):
        result.append(right[r])
        answer.append(right[r])
        check_cnt(right[r])
        r += 1

    return result


answer = merge_sort(arr)
print(num)
