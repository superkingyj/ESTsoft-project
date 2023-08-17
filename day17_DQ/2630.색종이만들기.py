import sys

N = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
blue_cnt, white_cnt = 0, 0
cnt = 0


def check(x, y, w, color):
    for i in range(x, x + w):
        for j in range(y, y + w):
            if grid[i][j] != color:
                return False
    return True


def devide(x, y, w):
    global white_cnt, blue_cnt

    color = grid[x][y]
    if check(x, y, w, color):
        if color == 1:
            blue_cnt += 1
        elif color == 0:
            white_cnt += 1
        return

    tmp = w // 2
    # 1구역
    devide(x, y, tmp)
    # 2구역
    devide(x, y + tmp, tmp)
    # 3구역
    devide(x + tmp, y, tmp)
    # 4구역
    devide(x + tmp, y + tmp, tmp)


devide(0, 0, N)
print(white_cnt)
print(blue_cnt)