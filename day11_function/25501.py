import sys

T = int(sys.stdin.readline())
cnt = 0

def recursion(string, left, right):
    global cnt
    if left >= right: return 1
    elif string[left] != string[right]: return 0
    else: 
        cnt += 1
        return recursion(string, left+1, right-1) 

def is_palindrome(string):
    return (recursion(string, 0, len(string)-1), cnt)

for _ in range(T):
    cnt = 1
    string = sys.stdin.readline().rstrip()
    print(*is_palindrome(string))