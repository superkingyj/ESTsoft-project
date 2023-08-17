from collections import deque


def bfs(graph, start):
    q = deque()
    visited = set()
    queue = deque([start])

    while queue:
        # 여기가 dfs와 차이점
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            queue.extend(graph[node] - visited)


graph = {
    "A": set(["B", "C"]),
    "B": set(["A", "D", "E"]),
    "C": set(["A", "F"]),
    "D": set(["B"]),
    "E": set(["B", "F"]),
    "F": set(["C", "E"]),
}

bfs(graph, "A")
