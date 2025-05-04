import heapq

def prims(graph):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    mst_edges = []
    total_weight = 0
    
    min_heap = []
    heapq.heappush(min_heap, (0, 0, -1))
    
    while min_heap:
        weight, curr_node, parent_node = heapq.heappop(min_heap)
        
        if visited[curr_node]:
            continue
        
        visited[curr_node] = True
        if parent_node != -1:
            mst_edges.append((parent_node, curr_node, weight))
            total_weight += weight
            
        for neighbor, edge_weight in graph[curr_node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor, curr_node))
                
    return mst_edges, total_weight
    
graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}

mst_edges, total_weight = prims(graph)

print("Edges in MST:")
for u, v, w in mst_edges:
    print(f"{u} -- {v} == {w}")
print(f"Total weight: {total_weight}")
        
    