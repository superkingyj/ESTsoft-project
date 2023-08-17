# dfs는 stack과 유사


def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        # 여기가 bfs와 차이점
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            stack.extend(graph[node] - visited)


graph = {
    1: set([1, 2]),
    2: set(["A", "D", "E"]),
    3: set(["A", "F"]),
    4: set(["B"]),
    5: set(["B", "F"]),
    6: set(["C", "E"]),
}

dfs(graph, "A")
