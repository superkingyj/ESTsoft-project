import sys

N, M = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))


# t시간에 n명을 태울 수 있는지 확인하는 함수
def get_cnt(mid):
    cnt = M
    for time in times:
        cnt += mid // time
    return cnt


def binaray_search():
    left, right = 1, 2_000_000_000 * 30
    result_time = float("inf")

    while left <= right:
        mid = (left + right) // 2
        cnt = get_cnt(mid)

        if cnt >= N:
            result_time = min(result_time, mid)
            right = mid - 1
        else:
            left = mid + 1

    return result_time


if N <= M:
    print(N)
else:
    result_time = binaray_search()
    # print(result_time)
    children = M

    # result_time-1 시간동안에 탄 아이들의 총합 구하기
    for i in range(M):
        children += (result_time - 1) // times[i]

    # result_time에 탄 아이들 구하기
    for i in range(M):
        if result_time % times[i] == 0:
            children += 1
        # 만약 마지막 아이라면
        if children == N:
            print(i + 1)
            break
