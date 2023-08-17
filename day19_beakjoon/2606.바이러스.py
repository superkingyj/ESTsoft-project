import sys
from collections import defaultdict, deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)


def bfs():
    q = deque()
    visited = [True] + [False] * N
    visited[1] = True
    q.append(1)
    result = 0

    while q:
        v = q.popleft()
        if v != 1:
            result += 1

        for _v in graph[v]:
            if not visited[_v]:
                visited[_v] = True
                q.append(_v)

    return result


print(bfs())
