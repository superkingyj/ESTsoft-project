import sys

X, Y = sys.stdin.readline().rstrip().split()

rev_x=X[::-1]
rev_y=Y[::-1]

rev_x_y = int(str(int(rev_x) + int(rev_y))[::-1])
print(rev_x_y)
