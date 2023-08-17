import sys

arr = sys.stdin.readline().rstrip().split("-")
sum_val = 0

for num in arr[0].split("+"):
    sum_val += int(num)

for string in arr[1:]:
    for num in string.split("+"):
        sum_val -= int(num)

print(sum_val)
