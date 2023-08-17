# left = mid, right = mid로 하면 계속 같은 값으로 고정 되어서 무한루프에 빠질 수 있음
# 따라서 mid값을 한칸 이동하면 됨


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


arr = [1, 3, 2, 6, 7, 10, 11, 8, 5]
arr.sort()

result = binary_search(arr, 12)
print(result)
