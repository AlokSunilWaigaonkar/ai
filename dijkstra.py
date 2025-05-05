import heapq

def dijkstra(graph,start):
	dist = {node : float('inf') for node in graph}
	dist[start] = 0
	pq = [(0,start)]
	
	while pq:
		cost , u = heapq.heappop(pq)
		
		for v,weight in graph[u]:
			if dist[u]+weight < dist[v]:
				dist[v] = dist[u] + weight
				heapq.heappush(pq , (dist[v],v))
				
	return dist
				
	
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

dijkstra(graph, 'A')


shortest_paths = dijkstra(graph, 'A')
print("Shortest distances from A:")
for node, distance in shortest_paths.items():
    print(f"A → {node} = {distance}")

