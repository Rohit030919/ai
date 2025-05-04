class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]  # Each node is its own parent initially
    
    def find(self, x):
        '''Find the root parent of node x'''
        while self.parent[x] != x:
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        '''Connect two components'''
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:  # Only connect if they're in different components
            self.parent[root_x] = root_y
            return True  # Successfully connected
        return False  # Already connected (would form a cycle)

def kruskal_mst(num_nodes, edges):
  
    # Step 1: Sort all edges by weight (smallest first)
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    uf = UnionFind(num_nodes)
    mst_edges = []
    total_weight = 0
    
    # Step 2: Process each edge in order
    for edge in sorted_edges:
        node1, node2, weight = edge
        
        # Check if adding this edge would create a cycle
        if uf.union(node1, node2):
            # No cycle created, so add to MST
            mst_edges.append(edge)
            total_weight += weight
            
            # Early exit if we've connected all nodes
            if len(mst_edges) == num_nodes - 1:
                break
    
    return mst_edges, total_weight

# Example Usage
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, total_weight = kruskal_mst(4, edges)
print("MST Edges:", mst)
print("Total Weight:", total_weight)
