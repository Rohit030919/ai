def astaralgo(start, goal):
    open_set = [start]
    g_cost = {start:0}
    parents = {start:None}
    
    while open_set:
        current = open_set[0]
        
        for node in open_set:
            if g_cost[node] + heuristic(node) < g_cost[current] + heuristic(current):
                current = node
                
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            path.reverse()
            print("Path Found:", path)
            return path
            
        open_set.remove(current)
        
        for neighbor, cost in get_neighbor(current):
            new_g = g_cost[current] + cost
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parents[neighbor] = current
                if neighbor not in open_set:
                    open_set.append(neighbor)
                   
    print("Path does not exist")
    return None
    
def get_neighbor(node):
    return Graph_nodes.get(node, [])
    
def heuristic(node):
    H = {
    'Home':120,
    'Bank':80,
    'Garden':100,
    'School':70,
    'RailwayStation':20,
    'PostOffice':110,
    'PoliceStation':26,
    'University':0
    }
    return H.get(node, float('inf'))

Graph_nodes = {
    'Home': [('Bank', 45), ('Garden', 40), ('School', 50)],
    'Bank': [('PoliceStation', 60)],
    'Garden': [('RailwayStation', 72)],
    'School': [('RailwayStation', 75), ('PostOffice', 59)],
    'PoliceStation': [('University', 28)],
    'RailwayStation': [('University', 40)],
    'PostOffice': [],
    'University': []
}

astaralgo('Home','University')