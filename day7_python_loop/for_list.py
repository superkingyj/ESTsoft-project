import sys
import os

# fruits = ["사과🍎", "맹고🥭", "수박🍉"]

# for fruit in fruits:
#     print(fruit)

# for i in range(0,5):
#     print(i)

# fruits = ["사과🍎", "맹고🥭", "수박🍉"]
# prices = [2500, 15000, 5000]
# amounts = [4, 5, 3]

# for fruit, price, amount in zip(fruits, prices, amounts):
#     profit = price * amount
#     print(f"{fruit}: {price}원, 재고 {amount}개, 수익금 {profit}원")
# 
# for i in range(0, 10):
#     if i == 5: break
#     print(i)


with open("day7_python_loop/text.txt", "r", encoding='utf-8') as f:
    text = f.read().split('\n')
    for idx, line in enumerate(text):
        name, score = line.split()
        print(f"{idx+1}번째 학생: {name}, 점수: {score}")


# a = "Hello World!"
# length = 0

# for char in a:
#     length += 1

# print(length)


# a = ["1","2","3","4","5"]
# b = list(map(int, a))
# print(b)
# sum_val = 0

# for val in a:
#     sum_val += int(val)

# print(sum_val)

# n = int(sys.stdin.readline())
# dp = [0 for _ in range(n+1)]
# dp[0] = 1

# for i in range(1, n+1):
#     dp[i] = dp[i-1] * i

# factorial = dp[n]
# print(factorial)

