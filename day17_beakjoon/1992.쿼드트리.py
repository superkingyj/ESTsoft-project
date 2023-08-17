import sys

N = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(N)]


def check(x, y, w, dot):
    for i in range(x, x + w):
        for j in range(y, y + w):
            if grid[i][j] != dot:
                return False
    return True


def devide(x, y, w):
    dot = grid[x][y]
    if check(x, y, w, dot):
        if dot == "1":
            print(1, end="")
        elif dot == "0":
            print(0, end="")
        return

    print("(", end="")
    tmp = w // 2
    devide(x, y, tmp)
    devide(x, y + tmp, tmp)
    devide(x + tmp, y, tmp)
    devide(x + tmp, y + tmp, tmp)
    print(")", end="")


devide(0, 0, N)
