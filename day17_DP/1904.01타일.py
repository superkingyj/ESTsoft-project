import sys

N = int(sys.stdin.readline())

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    DP = [0] * (N + 1)
    DP[1], DP[2] = 1, 2
    for i in range(3, N + 1):
        DP[i] = (DP[i - 1] + DP[i - 2]) % 15746  # 나머지를 더해주면 나머지가 계속 남음

    print(DP[-1])


"""
나머지는 보존됨
1/3 ... 1
2/3 ... 2
3/3 ... 0(1 + 2 => 3 % 3 = 0)
4/3 ... 1
5/3 ... 2 
6/3 ... 0 
"""
