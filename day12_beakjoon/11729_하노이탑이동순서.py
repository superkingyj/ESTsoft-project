import sys

N = int(sys.stdin.readline())


def move(start, end):
    print(start, end)


def hanoi(n, start, via, end):
    if n == 1:
        move(start, end)
        return

    hanoi(n - 1, start, end, via)
    move(start, end)
    hanoi(n - 1, via, start, end)


print(2**N - 1)
hanoi(N, 1, 2, 3)
