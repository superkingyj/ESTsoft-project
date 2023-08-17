import sys

N = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
blue_cnt, white_cnt, red_cnt = 0, 0, 0
cnt = 0


def check(x, y, w, color):
    for i in range(x, x + w):
        for j in range(y, y + w):
            if grid[i][j] != color:
                return False
    return True


def devide(x, y, w):
    global white_cnt, blue_cnt, red_cnt

    color = grid[x][y]
    if check(x, y, w, color):
        if color == 1:
            blue_cnt += 1
        elif color == 0:
            white_cnt += 1
        elif color == -1:
            red_cnt += 1
        return

    for i in range(3):
        for j in range(3):
            devide(x + (w // 3) * i, y + (w // 3) * j, w // 3)


devide(0, 0, N)
print(red_cnt)
print(white_cnt)
print(blue_cnt)
