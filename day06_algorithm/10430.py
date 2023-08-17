import sys

one = sys.stdin.readline().rstrip()
two = sys.stdin.readline().rstrip()

print(int(one) * int(two[2]))
print(int(one) * int(two[1]))
print(int(one) * int(two[0]))
print(int(one) * int(two))