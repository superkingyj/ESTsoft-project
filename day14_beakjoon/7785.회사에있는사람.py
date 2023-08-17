import sys

N = int(sys.stdin.readline())
info = dict()

for _ in range(N):
    name, status = sys.stdin.readline().strip().split()
    info[name] = status

for name, status in sorted(list(info.items()), reverse=True):
    if status == "enter":
        print(name)
