def is_safe(node,graph,color,c):
	for neighbour in graph[node]:
		if color[neighbour] == c:
			return False
	return True
	

def solve_graph_coloring(graph,m,color,node):
	if node == len(graph):
		return True
		
	for c in range(1,m+1):
		if is_safe(node,graph,color,c):
			color[node] = c
			if solve_graph_coloring(graph,m,color,node+1):
				return True
			color[node] = 0
			
	return False
	

def printSolution(color):
	print("Color assignment to the nodes:")
	for i,c in enumerate(color):
		print(f"Node{i} --> Color{c}")

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
    printSolution(color)
else:
    print("No solution exists.")