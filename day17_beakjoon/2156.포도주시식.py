import sys

N = int(sys.stdin.readline())
arr = [0] + list(int(sys.stdin.readline()) for _ in range(N))

if N == 1:
    print(arr[1])
elif N == 2:
    print(sum(arr))
elif N == 3:
    print(max(arr[1] + arr[2], arr[2] + arr[3]))
else:
    DP = [0] * (N + 1)
    DP[1] = arr[1]
    DP[2] = arr[1] + arr[2]

    for i in range(3, N + 1):
        DP[i] = max(DP[i - 2], arr[i - 1] + DP[i - 3]) + arr[i]
        DP[i] = max(DP[i], DP[i - 1])

    print()
    print(max(DP))
