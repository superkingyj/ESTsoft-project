# 피보나치 수열: 직전의 두 수를 더해서 현재 수가 만들어지는 수열

import sys

N = int(sys.stdin.readline())
fibo = [0 for _ in range(N+1)]
fibo[0], fibo[1] = 0, 1 

for i in range(2, N+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo)
print(fibo[N])