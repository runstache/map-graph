'''
Tests for the Graph Structure Class
'''

from structures.graph import Graph
from structures.node import Node
import uuid

from assertpy import assert_that

def test_constructor():
    '''
    Tests Graph Constructor.
    '''
    
    g = Graph()
    
    assert_that(g, 'A new instance of a Graph can be created').is_not_none()
    
def test_add_vertex():
    '''
    Tests adding a vertext to the graph.
    '''
    
    vtex = {
        'id': 1234,
        'name': 'test'
    }
    
    n = Node(str(uuid.uuid4()), 'TestNode', vtex)
    
    g = Graph()
    g.add_vertex(n)
    
    assert_that(g.n, 'Number of vertexes should be 1').is_equal_to(1)

def test_add_edge():
    '''
    Tests adding an edge to the graph
    '''
    
    item = {
        'id': 1234,
        'name': 'test1'
    }
    
    vtex = {
        'id': 567,
        'name': 'test2'
    }
    
    n1 = Node(str(uuid.uuid4()), 'TestObject', item)
    n2 = Node(str(uuid.uuid4()), 'TestObject', vtex)
    
    g = Graph()
    g.add_edge(n1, n2)
    
    assert_that(g.n, 'Number of vertices should be 2').is_equal_to(2)
    assert_that(g.m, 'Number of edges should be 1').is_equal_to(1)
    
def test_remove_edge() :
    '''
    Tests Removing an Edge
    '''
    
    item = {
        'id': 1234,
        'name': 'test1'
    }
    
    vtex = {
        'id': 567,
        'name': 'test2'
    }
    
    item2 = {
        'id': 14556,
        'name': 'test3'
    }
    
    n1 = Node(str(uuid.uuid4()), 'TestObject', item)
    n2 = Node(str(uuid.uuid4()), 'TestObject', vtex)
    n3 = Node(str(uuid.uuid4()), 'TestObject', item2)
    
    g = Graph()
    g.add_edge(n1, n2)
    g.add_edge(n2, n3)
    
    assert_that(g.n, 'Number of vertices should be 3').is_equal_to(3)
    assert_that(g.m, 'Number of edges should be 2').is_equal_to(2)
    
    g.remove_edge(n2, n1)
    
    assert_that(g.m, 'Number of edges should be 1').is_equal_to(1)
    
def test_remove_vertex():
    '''
    Tests removing a vertex from the graph.
    '''
    
    
    item = {
        'id': 1234,
        'name': 'test1'
    }
    
    vtex = {
        'id': 567,
        'name': 'test2'
    }
    
    item2 = {
        'id': 14556,
        'name': 'test3'
    }
    
    n1 = Node(str(uuid.uuid4()), 'TestObject', item)
    n2 = Node(str(uuid.uuid4()), 'TestObject', vtex)
    n3 = Node(str(uuid.uuid4()), 'TestObject', item2)
    
    g = Graph()
    g.add_edge(n1, n2)
    g.add_edge(n2, n3)
    
    assert_that(g.n, 'Number of vertices should be 3').is_equal_to(3)
    assert_that(g.m, 'Number of edges should be 2').is_equal_to(2)
    
    g.remove_vertex(n2)
    
    assert_that(g.n, 'Number of vertices should be 2').is_equal_to(2)
    assert_that(g.m, 'Number of edges should be 0').is_equal_to(0)
    