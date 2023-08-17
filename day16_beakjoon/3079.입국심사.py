import sys

def is_possible(minutes, times, n):
    return sum([minutes // time for time in times]) >= n

def solution(n, times):
    times.sort()
    left, right = times[0], times[0] * n
    answer = float("inf")

    while left <= right:
        mid = (left + right) // 2

        if is_possible(mid, times, n):
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1

    return answer

N, M = map(int, sys.stdin.readline().split())
T = [int(sys.stdin.readline()) for _ in range(N)]
print(solution(M, T))