from collections import deque

class Graph:

	def __init__(self, edges, n):
		self.adjList = [[] for _ in range(n)]  
		
		for (src, dest) in edges:
			self.adjList[src].append(dest)
			self.adjList[dest].append(src)

		def print_graph(self):
			for i, neighbors in enumerate(self.adjList):
				print(f"Adjacency list of vertex {i}: {neighbors}")
			
			

def DFS(graph, v, discovered):
	discovered[v] = True  
	print(v, end=' ')   	

	for u in graph.adjList[v]:  
		if not discovered[u]:   
			DFS(graph, u, discovered) 


def recursiveBFS(graph, q, discovered):
	
	if not q:
		return
	
	v = q.popleft()
	print(v, end=' ')

	for u in graph.adjList[v]:
		if not discovered[u]:
			
			discovered[u] = True
			q.append(u)

	
	recursiveBFS(graph, q, discovered)

if __name__ == '__main__':
		# creating options  
	while True: 
		edges = [
			(1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
			(3, 5), (8, 9), (8, 12), (9, 7), (9, 11)
		]

		n = 13
		graph = Graph(edges, n)  
				
		print("WELCOME TO A SIMPLE MENSURATION PROGRAM")  
	
 
		print("\nMAIN MENU")  
		print("1. Print Graph") 
		print("2. DFS Traversal")  
		print("3. BFS Traversal")  
		print("4. Exit")  
		choice = int(input("Enter the Choice:")) 

		if choice == 1:
			print("Graph:")
			graph.print_graph() 
		
		elif choice == 2:
			discovered = [False] * n 
			for i in range(n):
				if not discovered[i]:  
					DFS(graph, i, discovered)  

		elif choice == 3:
			discovered = [False] * n	
			q = deque()
			for i in range(n):
				if not discovered[i]:	
					discovered[i] = True
					q.append(i)			
					recursiveBFS(graph, q, discovered)
					
		elif choice == 4:
			print("Thanks for Using this program.")  
			break  
              
		else:  
			print("Oops! Incorrect Choice.")

























