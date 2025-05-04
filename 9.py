def is_safe(node, graph, color, c):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True


def solve_graph_coloring(graph, m, color, node):
    if node == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(node, graph, color, c):
            color[node] = c
            if solve_graph_coloring(graph, m, color, node + 1):
                return True
            color[node] = 0  # Backtrack
    return False


def print_solution(color):
    print("Color assignment to nodes:")
    for i, c in enumerate(color):
        print(f"Node {i} ---> Color {c}")


# Example usage
# Graph represented as adjacency list
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

num_colors = 3  # Try with 2 or 3
num_nodes = len(graph)
color = [0] * num_nodes

if solve_graph_coloring(graph, num_colors, color, 0):
    print_solution(color)
else:
    print("No solution exists.")