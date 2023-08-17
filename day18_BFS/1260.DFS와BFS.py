import sys
from collections import defaultdict
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = []

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)


def init_viisted():
    global visited
    visited = [True] + [False] * N


def dfs(v):
    global visited

    print(v, end=" ")
    visited[v] = True

    graph[v].sort()
    for _v in graph[v]:
        if visited[_v]:
            continue
        dfs(_v)


def bfs(v):
    q = deque()
    visited[v] = True
    q.append(v)

    while q:
        v = q.popleft()
        print(v, end=" ")

        graph[v].sort()
        for _v in graph[v]:
            if visited[_v]:
                continue
            visited[_v] = True
            q.append(_v)


init_viisted()
dfs(V)
print()
init_viisted()
bfs(V)
