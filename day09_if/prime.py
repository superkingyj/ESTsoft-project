n = int(input())

is_prime = True
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        is_prime = False
        break

print("소수 맞음") if is_prime else print("소수 아님")

