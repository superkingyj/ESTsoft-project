import sys

string = sys.stdin.readline().rstrip()
n = len(string)
is_palindrom = True

for i in range(n):
    if string[i] != string[n-1-i]:
        is_palindrom = False

print(1) if is_palindrom else print(0)
