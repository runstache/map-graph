# Map Graph

Python simple Graph implementation for lightweight object mapping.

## Usage

The graph leverages two dictionaries to keep track of the nodes and edges of the graph. Each node is expected to be referenced by a canonical id which is unique across the graph. Relationships are then established using these canonical ids.

### Examples

You can create a graph and add nodes by doing the following:

```python

from src.structures.mapping import Graph, MissingNodeError


graph = Graph('urn:oid:2.1.2.5565894.456')

loinc_id = 'http://www.loinc.org/10234-3'
loinc_code = {
    'code': '10234-3'
    'description': 'Sample Loinc Code'
}

person_id = 'urn:oid:2.1.3345.3234.2.1:33454'
person_node = {
    'name': 'jim smith',
    'age': 25,
}

graph.add_node(loinc_id, loinc_code)
graph.add_node(person_id, person_node)
graph.add_relationship(loinc_id, person_id)

```

Nodes are references by the canonical id.  Retrieving these items can be accomplished through the __get_node__ method:

```python

person_id = 'urn:oid:2.1.3345.3234.2.1:33454'

person_node = graph.get_node(person_id)

```

Nodes that do not exist in the graph will return a __MissingNodeError__ when there is an attempt to create a relationship with or retrieve a node by canonical id that does not exist.

```python
from src.structures.mapping import Graph, MissingNodeError
import logging

graph = Graph('urn:oid:2.1.2.5565894.456')

loinc_id = 'http://www.loinc.org/10234-3'
loinc_code = {
    'code': '10234-3'
    'description': 'Sample Loinc Code'
}

person_id = 'urn:oid:2.1.3345.3234.2.1:33454'
person_node = {
    'name': 'jim smith',
    'age': 25,
}

graph.add_node(person_id, person_node)

try:
    graph.add_relationship([loinc_id, person_id])

except MissingNodeError as err:
    logging.error(err.message)
    
```

