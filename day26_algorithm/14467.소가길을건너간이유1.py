import sys

N = int(sys.stdin.readline())
pos_info = dict()

for _ in range(N):
    cow, pos = map(int, sys.stdin.readline().split())
    if cow not in pos_info:
        pos_info[cow] = (0, pos)
    elif pos_info[cow][1] != pos:
        pos_info[cow] = (pos_info[cow][0] + 1, pos)

print(sum(val[0] for val in pos_info.values()))
