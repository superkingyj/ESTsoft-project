import sys

T = int(sys.stdin.readline())


def dynamic_programming():
    DP = [0] * 101
    DP[0] = 1
    DP[1] = 1
    DP[2] = 1
    DP[3] = 1
    DP[4] = 2
    DP[5] = 2

    for i in range(6, 101):
        DP[i] = DP[i - 1] + DP[i - 5]
    return DP


DP = dynamic_programming()

for _ in range(T):
    N = int(sys.stdin.readline())
    print(DP[N])
