import heapq

def astar(start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic(start), 0, start))  # (f(n), g(n), node)
    
    g_cost = {start: 0}
    parents = {start: None}
    
    while open_set:
        _, current_g, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            path.reverse()
            print("Path Found:", path)
            return path
        
        for neighbour, cost in get_neighbour(current):
            new_g = g_cost[current] + cost
            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g
                parents[neighbour] = current
                f = new_g + heuristic(neighbour)
                heapq.heappush(open_set, (f, new_g, neighbour))

    print("Path not found")
    return None


def get_neighbour(node):
    return Graph_nodes.get(node, [])


def heuristic(node):
    H = {
        'Home': 120,
        'Bank': 80,
        'Garden': 100,
        'School': 70,
        'RailwayStation': 20,
        'PostOffice': 110,
        'PoliceStation': 26,
        'University': 0
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

astar('Home', 'University')