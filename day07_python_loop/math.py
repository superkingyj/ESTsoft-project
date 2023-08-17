import sys


# 최대공약수
def get_greatest_common_division():
    while b != 0:
        a, b = b, a%b

    gcd = a
    return gcd


# 최소 공배수
def get_gretest_common_multiple():
    lcd = int(a * b / gcd)
    return lcd


# 소인수 분해
def get_factorizaion(n):
    factors = []

    # 1. 2로 나눠주기
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    i = 3
    # 2. 나누는 값보다 몫이 클 때 까지
    while i * i <= n: 
        while n % i == 0: 
            factors.append(i)
            n //= i 
        i += 2
    
    return factors

a, b = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
gcd = get_greatest_common_division()
lcd = get_gretest_common_multiple()
factor = get_factorizaion(n)

