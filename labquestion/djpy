# Dijkstra's Shortest Path Algorithm

# Graph represented using an adjacency matrix
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

n = len(graph)

# Take source vertex
source = int(input("Enter source vertex (0-8): "))

# Initialize distances and visited array
dist = [float('inf')] * n
visited = [False] * n

dist[source] = 0

# Dijkstra's Algorithm
for _ in range(n):

    # Find unvisited vertex with minimum distance
    min_dist = float('inf')
    u = -1

    for i in range(n):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i

    if u == -1:
        break

    visited[u] = True

    # Update distances of adjacent vertices
    for v in range(n):
        if graph[u][v] > 0 and not visited[v]:

            new_dist = dist[u] + graph[u][v]

            if new_dist < dist[v]:
                dist[v] = new_dist

# Display shortest distances
print("\nShortest distances from vertex", source)

for i in range(n):
    print("Vertex", i, ":", dist[i])