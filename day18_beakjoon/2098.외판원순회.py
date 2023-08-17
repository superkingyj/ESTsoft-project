import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_cost = sys.maxsize


def can_go(s_v, e_v):
    if visited[e_v]:
        return False
    if graph[s_v][e_v] == 0:
        return False
    return True


def dfs(start, curr, depth, cost):
    global min_cost

    # 모든 곳에 방문했고
    if depth == N:
        # 현재 방문지에서 출발지로 가는 경로가 없다면 중지
        if graph[curr][start] == 0:
            return

        cost += graph[curr][start]
        # 최소 비용 갱신
        min_cost = min(min_cost, cost)
        return

    # 현재 비용이 최소 비용보다 크면 탐색 중지
    if cost > min_cost:
        return

    for i in range(N):
        if can_go(curr, i):
            visited[i] = True
            dfs(start, i, depth + 1, cost + graph[curr][i])
            visited[i] = False


for i in range(N):
    visited = [False] * N
    visited[i] = True
    dfs(i, i, 1, 0)

print(min_cost)
