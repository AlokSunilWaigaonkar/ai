def kruskal(graph):
	parent = {}
	
	def find(x):
		while parent[x]!=x:
			x=parent[x]
		return x
		
	def union(x,y):
		parent[find(x)] = find(y)
		
	unique_edges = set()
	for u in graph:
		for v,weight in graph[u]:
			if (weight, v, u) not in unique_edges:
				unique_edges.add((weight, u,v))
	
	sorted_edges = sorted(unique_edges)	
	for node in graph:
		parent[node] = node
			
	mst = []
	total_cost = 0
	
	for weight , u ,v in sorted_edges:
		if find(u) != find(v):
			union(u,v)
			mst.append((u,v))
			total_cost+=weight
			
	print("MST : ",mst)
	print("Total cost :",total_cost)
	
graph = {
    'A': [('B', 1), ('D', 5)],
    'B': [('A', 1), ('C', 3), ('D', 2), ('E', 4)],
    'C': [('B', 3), ('E', 1)],
    'D': [('A', 5), ('B', 2), ('F', 4)],
    'E': [('B', 4), ('C', 1), ('G', 6)],
    'F': [('D', 4), ('G', 2)],
    'G': [('E', 6), ('F', 2)]
}

kruskal(graph)
			
			