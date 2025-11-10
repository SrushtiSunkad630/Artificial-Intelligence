from collections import deque


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': [],
    'F': ['K'],
    'G': [],
    'H': [],
    'I': [],
    'K': []
}
#DFS
def dfs_full(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=" ")   

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_full(graph, neighbor, visited)

print("DFS Full Traversal Order:")
dfs_full(graph, 'A')


#DLS
def dls(graph, node, goal, limit, path=None):
    if path is None:
        path = []

    path.append(node)

    if node == goal:
        return path
    
    if limit <= 0:
        return None

    for neighbor in graph[node]:
        result = dls(graph, neighbor, goal, limit - 1, path.copy())
        if result:
            return result
    
    return None

#BFS
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                queue.append(new_path)

    return None



print("DFS Path A→G:", dfs(graph, 'A', 'G'))
print("DLS Path A→G (limit=2):", dls(graph, 'A', 'G', 2))
print("BFS Path A→G:", bfs(graph, 'A', 'G'))



OUTPUT
DFS Full Traversal Order:
A B D H I E C F K G DFS Path A→G: ['A', 'C', 'G']
DLS Path A→G (limit=2): ['A', 'C', 'G']
BFS Path A→G: ['A', 'C', 'G']
