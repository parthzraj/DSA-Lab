def bfs(graph, start):
    visited = []
    queue = [start]

    print("BFS Traversal:")

    while queue:
        node = queue.pop(0)

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)


def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')

print("\nDFS Traversal:")
dfs(graph, 'A', [])