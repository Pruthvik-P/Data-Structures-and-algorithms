from collections import defaultdict

class Graph:
  def __init__(self):
    self.adjacency_list = defaultdict(list)

  def add_vertex(self, vertex):#func for adding a node
    if vertex not in self.adjacency_list:
      self.adjacency_list[vertex] = []

  def remove_vertex(self, vertex):#func for removing a node
    if vertex not in self.adjacency_list:
      return
    self.adjacency_list.pop(vertex)
    for neighbors in self.adjacency_list.values():
      if vertex in neighbors:
        neighbors.remove(vertex)

  def add_edge(self,vertex1, vertex2):#func for adding an edge
    self.adjacency_list[vertex1].append(vertex2)
    self.adjacency_list[vertex2].append(vertex1)

  def remove_edge(self, vertex1, vertex2):#func for removing an edge
    self.adjacency_list[vertex1].remove(vertex2)
    self.adjacency_list[vertex2].remove(vertex1)

  def get_vertices(self): # func to list all the nodes
    return list(self.adjacency_list.keys())

  def get_edges(self): # func to list all the edges
    edges = []
    for vertex, neighbors in self.adjacency_list.items():
      for neighbor in neighbors:
        if vertex < neighbor:
          edges.append((vertex, neighbor))
    return edges

  def get_neighbors(self, vertex):#func to list all the neighbors
    return self.adjacency_list[vertex]

  def is_adjacent(self, vertex1, vertex2):#func to check if two nodes are adjacent
    return vertex2 in self.adjacency_list[vertex1]

  def get_vertex_count(self):#func to get the number of nodes
    return len(self.adjacency_list)

  def get_edge_count(self):#func to get the number of edges  
    count = sum(len(neighbour) for neighbour in self.adjacency_list.values())
    return count // 2

graph = Graph()
vertices = [1, 2, 3, 4, 5, 6]
edges = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6)]

for v in vertices:
  graph.add_vertex(v)

for edge in edges:
  graph.add_edge(*edge)

print(f"Vertices: {graph.get_vertices()}")
print(f"Edges: {graph.get_edges()}")
print(f"Neighbors of 1: {graph.get_neighbors(1)}")
print(f"Is 1 adjacent to 2? {graph.is_adjacent(1, 2)}")

graph.remove_edge(1, 2)
graph.remove_vertex(3)

print("After removing an edge and vertex:")
print(f"Vertices: {graph.get_vertices()}") 
print(f"Edges: {graph.get_edges()}")