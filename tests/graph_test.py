"""
Tests for the Graph Structure.    
"""

from assertpy import assert_that
from src.structures.mapping import Graph, MissingNodeError
from uuid import uuid4

def test_add_node():
    """
    Tests adding a Node to the graph.
    """
    
    canonical_id = 'urn:uuid:' + str(uuid4())
    graph = Graph(canonical_id)
    
    node_id = 'urn:uuid:' + str(uuid4())
    node = {
        'key1': 'my_value',
        'key2': 'my_value2'
    }
    
    graph.add_node(node_id, node)
    
    result = graph.get_node(node_id)
    
    assert_that(result)\
        .is_not_none()\
        .is_type_of(dict)\
        .contains_entry({'key1': 'my_value'})\
        .contains_entry({'key2':'my_value2'})
        
def test_get_node_not_present():
    """
    Tests retrieving a node value from the graph.
    """
    
    canonical_id = 'urn:uuid:' + str(uuid4())
    graph = Graph(canonical_id)
    
    node_id = 'urn:uuid:' + str(uuid4())
    node = {
        'key1': 'my_value',
        'key2': 'my_value2'
    }
    
    graph.add_node(node_id, node)
    
    assert_that(graph.get_node).raises(MissingNodeError).when_called_with(str(uuid4()))
    
    
def test_add_relationship():
    """
    Tests adding a node to the graph where both nodes exist.
    """
    
    graph_id = 'urn:uuid:' + str(uuid4())
    graph = Graph(graph_id)
    
    node1_id = 'urn:uuid:' + str(uuid4())
    node1 = {
        'node': 1
    }
    
    node2_id = 'urn:uuid:' + str(uuid4())
    node2 = {
        'node': 2
    }
    
    graph.add_node(node1_id, node1)
    graph.add_node(node2_id, node2)
    
    graph.add_relationship([node1_id, node2_id])
    
    result = graph.get_relationships(node1_id)
    
    assert_that(result).is_not_empty().contains(node2_id)
    
    result = graph.get_relationships(node2_id)
    assert_that(result).is_not_empty().contains(node1_id)
    
    
def test_add_relationship_missing_node():
    """
    Tests a Missing Node Error is returned when a 
    node does not exist in a relationship add.
    """
    
    graph_id = 'urn:uuid:' + str(uuid4())
    graph = Graph(graph_id)
    
    node1_id = 'urn:uuid:' + str(uuid4())
    node1 = {
        'node': 1
    }
    
    node2_id = 'urn:uuid:' + str(uuid4())
    
    graph.add_node(node1_id, node1)
    
    assert_that(graph.add_relationship).raises(MissingNodeError).when_called_with([node1_id, node2_id])

    
def test_nodes_property():
    """
    Tests retrieving the Nodes from the graph.
    """
    
    graph_id = 'urn:uuid:' + str(uuid4())
    graph = Graph(graph_id)
    
    node1_id = 'urn:uuid:' + str(uuid4())
    node1 = {
        'node': 1
    }
    
    node2_id = 'urn:uuid:' + str(uuid4())
    node2 = {
        'node': 2
    }
    
    graph.add_node(node1_id, node1)
    graph.add_node(node2_id, node2)
    
    result = graph.nodes
    
    assert_that(result)\
        .is_not_none()\
        .is_type_of(dict)\
        .contains_key(node1_id, node2_id)
    
    
def test_get_relationships():
    """
    Tests retrieving the relationships for a node in the graph.
    """
    
    graph_id = 'urn:uuid:' + str(uuid4())
    graph = Graph(graph_id)
    
    node1_id = 'urn:uuid:' + str(uuid4())
    node1 = {
        'node': 1
    }
    
    node2_id = 'urn:uuid:' + str(uuid4())
    node2 = {
        'node': 2
    }
    
    graph.add_node(node1_id, node1)
    graph.add_node(node2_id, node2)
    
    graph.add_relationship([node1_id, node2_id])
    
    result = graph.get_relationships(node1_id)
    
    assert_that(result)\
        .is_not_empty()\
        .is_length(1)\
        .contains(node2_id)\
        .does_not_contain(node1_id)
    
    
def test_get_relationships_no_node():
    """
    Tests that a Missing Node Error is returned
    when retreiving relationships for a node that does not exist.
    """
    
    graph_id = 'urn:uuid:' + str(uuid4())
    graph = Graph(graph_id)
    
    node1_id = 'urn:uuid:' + str(uuid4())
    node1 = {
        'node': 1
    }
    
    node2_id = 'urn:uuid:' + str(uuid4())
    node2 = {
        'node': 2
    }
    
    graph.add_node(node1_id, node1)
    graph.add_node(node2_id, node2)
    
    assert_that(graph.get_relationships).raises(MissingNodeError).when_called_with(str(uuid4()))
    
    
def test_node_count():
    """
    Tests the correct number of nodes are returned.
    """
    
    graph_id = 'urn:uuid:' + str(uuid4())
    graph = Graph(graph_id)
    
    node1_id = 'urn:uuid:' + str(uuid4())
    node1 = {
        'node': 1
    }
    
    node2_id = 'urn:uuid:' + str(uuid4())
    node2 = {
        'node': 2
    }
    
    graph.add_node(node1_id, node1)
    graph.add_node(node2_id, node2)
    graph.add_relationship([node1_id, node2_id])
    
    assert_that(graph.node_count).is_equal_to(2)
    
def test_edge_count():
    """
    Tests the correct number of edges are returned.
    """
    
    graph_id = 'urn:uuid:' + str(uuid4())
    graph = Graph(graph_id)
    
    node1_id = 'urn:uuid:' + str(uuid4())
    node1 = {
        'node': 1
    }
    
    node2_id = 'urn:uuid:' + str(uuid4())
    node2 = {
        'node': 2
    }
    
    node3_id = 'urn:uuid:' + str(uuid4())
    node3 = {
        'node': 3
    }
    
    
    graph.add_node(node1_id, node1)
    graph.add_node(node2_id, node2)
    graph.add_node(node3_id, node3)
    graph.add_relationship([node1_id, node2_id, node3_id])
    
    assert_that(graph.edge_count).is_equal_to(6)

def test_graph_canonical_id():
    """
    Tests the canonical url is returned.
    """    
    
    graph_id = 'urn:uuid:' + str(uuid4())
    graph = Graph(graph_id)
    
    assert_that(graph.canonical_id).is_equal_to(graph_id)

def test_missing_node_error():
    """
    Tests constructor for Missing Node Error
    """
    
    error = MissingNodeError('Node not found')
    
    assert_that(error.message).is_equal_to('Node not found')