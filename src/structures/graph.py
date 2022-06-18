'''
Graph Structure Definition
'''

from structures.node import Node

class Graph:
    
    def __init__(self):
        '''
        Initializes a Graph Structure.
        '''
        self.Edges = set()
        self._neighbors = {}      
          
    def add_vertex(self, vertex: Node):
        '''
        Adds a Vertex to the Graph
        '''
        if vertex not in self._neighbors:
            self._neighbors[vertex] = set()
        
        
    def add_edge(self, u: Node, v: Node):
        '''
        Adds a Edge for a given vertext
        '''
        
        self.add_vertex(u)
        self.add_vertex(v)
        self.Edges.add(frozenset([u,v]))
        self._neighbors[u].add(v)
        self._neighbors[v].add(u)
        
        
    def remove_edge(self, u: Node, v: Node):
        '''
        Removes an edge from the graph
        '''
        e = frozenset([u, v])
        if e in self.Edges:
            self.Edges.remove(e)
            self._neighbors[u].remove(v)
            self._neighbors[v].remove(u)
        
    def remove_vertex(self, vertex: Node):
        '''
        Removes a vertex from the graph
        '''
        to_delete = list(self.neighbors(vertex))
        for v in to_delete:
            self.remove_edge(v, vertex)
        del self._neighbors[vertex]
        
    @property
    def m(self):
        '''
        Returns the number of Edges
        '''
        return len(self.Edges)
    
    @property
    def n(self):
        '''
        Returns the number of Vertices.
        '''
        return len(self._neighbors)
        
    def deg(self, vertex: Node):
        '''
        Returns the degree of a vertex
        '''
        return len(self._neighbors[vertex])
    
    def neighbors(self, vertex: Node):
        '''
        Returns an iterator of the neighbors of a vertex.
        '''
        return iter(self._neighbors)
        
    
        