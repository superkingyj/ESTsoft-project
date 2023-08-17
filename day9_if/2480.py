import sys

num1, num2, num3 = map(int, sys.stdin.readline().split())

if num1 == num2 == num3: 
    print(10000 + num1*1000)
elif num1 == num2 and num2 != num3:
    print(1000 + num2*100)
elif num1 == num3 and num3 != num2:
    print(1000 + num3*100)
elif num2 == num3 and num3 != num1:
    print(1000 + num3*100)
else:
    print(max(num1, num2, num3)* 100)