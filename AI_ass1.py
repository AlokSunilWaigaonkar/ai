from collections import defaultdict , deque

graph = defaultdict(list)

def add_edge(u,v):
	graph[u].append(v)
	graph[v].append(u)

def dfs(node,visited):
	visited.add(node)
	print(node,end='')
	for neighbour in graph[node]:
		if neighbour not in visited:
			dfs(neighbour,visited)
			
			
def bfs(start):
	visited = set()
	queue = deque([start])
	visited.add(start)
	
	while queue:
		vertex=queue.popleft()
		print(vertex,end = '')
		for neighbour in graph[vertex]:
			if neighbour not in visited:
				visited.add(neighbour)
				queue.append(neighbour)
				
				
add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 3)
add_edge(1, 4)
add_edge(2, 5)
add_edge(2, 6)

print("DFS of undirected graph:")
dfs(0,set())

print("\nBFS of undirected graph:")
bfs(0)