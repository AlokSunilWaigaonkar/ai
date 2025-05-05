import heapq


def prims_algo(graph,start):
	
	visited = set()
	total_cost = 0
	min_heap = [(0,start,None)]
	mst_edges = []
	
	while min_heap:
		cost,u,parent = heapq.heappop(min_heap)
		if u not in visited:
			visited.add(u)
			total_cost+=cost
			if parent is not None:
				mst_edges.append((parent , u , cost))
			for v,weight in graph[u]:
				if v not in min_heap:
					heapq.heappush(min_heap,(weight,v,u))
	print("Minimum Spanning tree cost : ",total_cost)
	print("Minimum Spanning Tree :" , ) 
	for u ,v ,cost in mst_edges:
		print(f"{u} -- {v} (weight : {cost})")
		
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

prims_algo(graph, 'A') 
