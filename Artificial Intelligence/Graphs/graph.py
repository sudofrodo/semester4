class Vertex:
	def __init__(self, key):
		self.id = key
		self.connected_to = {}
	
	def add_neighbor(self,nbr,weight=0):
		self.connected_to[nbr] = weight

	def __str__(self):
		return str(self.id) + ' connected to ' + str([x.id for x in self.connected_to])

	def get_connections(self):
		return self.connected_to.keys()

	def get_id(self):
		return self.id

	def get_weight(self,nbr):
		return self.connected_to[nbr]

class Graph:
	def __init__(self):
		self.vert_list = {}
		self.num_of_vertices = 0

	def add_vertex(self,key):
		self.num_of_vertices = self.num_of_vertices + 1
		new_vertex = Vertex(key)
		self.vert_list[key] = new_vertex
		return new_vertex

	def get_vertex(self,n):
		if n in self.vert_list:
			return self.vert_list[n]
		else:
			return None

	def __contains__(self,n):
		return n in self.vert_list

	def add_edge(self,f,t,weight=0):
		if f not in self.vert_list:
			nv = self.add_vertex(f)
		if t not in self.vert_list:
			nv = self.add_vertex(t)
		self.vert_list[f].add_neighbor(self.vert_list[t],weight)

	def get_vertices(self):
		return self.vert_list.keys()

	def __iter__(self):
		return iter(self.vert_list.values())
	