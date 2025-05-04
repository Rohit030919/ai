import collections

def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start,end = " ")
    
    for next in graph[start] - visited:
        dfs(graph, next, visited)
        

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    
graph = {
    0:set([1,2]),
    1:set([3,4]),
    2:set([5,6]),
    3:set([]),
    4:set([]),
    5:set([]),
    6:set([])
}

print("DFS Traversal:")
dfs(graph, 0)

print("BFS Traversal:")
bfs(graph, 0)