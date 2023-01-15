"""
Mapping Classes.
"""


class MissingNodeError(Exception):
    """
    Missing Node Error Class.
    """

    __error__: str

    def __init__(self, error_message: str, *args: object) -> None:
        super().__init__(*args)
        self.__error__ = error_message

    @property
    def message(self) -> str:
        """
        Returns the Message from the Missing Node Error.
        """
        return self.__error__


class Graph:
    """
    Simple Node Graph with relationships.
    """

    __node_values__: dict
    __vertex_index__: dict
    __id__: str

    def __init__(self, canonical_id: str):
        """
        Constructor.
        """

        self.__node_values__ = {}
        self.__vertex_index__ = {}
        self.__id__ = canonical_id

    def add_node(self, canonical_id: str, value) -> None:
        """
        Adds a Node to the Graph.

        Args:
            canonical_id (str): Canonical Identifier
            value (any): Node Value
        """

        self.__node_values__[canonical_id] = value
        if canonical_id not in self.__vertex_index__:
            self.__vertex_index__[canonical_id] = set()

    def add_relationship(self, ids: list[str]) -> None:
        """
        Adds relationships between all ids in the list.
        If the ids is not in the graph, raises missing Node Exception

        Args:
            ids (list[str]): List of Ids.
        """

        for canonical_id in ids:
            if canonical_id not in self.__node_values__:
                raise MissingNodeError('Node not present in graph.')

            relationships = self.__vertex_index__.get(canonical_id, set())
            for item in ids:
                if item != canonical_id:
                    relationships.add(item)
            self.__vertex_index__[canonical_id] = relationships

    @property
    def canonical_id(self) -> str:
        """
        Returns the canonical id for the graph.

        Returns:
            str: Canonical id
        """
        return self.__id__

    @property
    def nodes(self) -> dict:
        """
        Returns a dictionary of all nodes be canonical id.

        Returns:
            dict: Dictionary
        """
        return dict(self.__node_values__)

    @property
    def node_count(self) -> int:
        """
        Returns the number of nodes in the graph.

        Returns:
            int: Count of Nodes.
        """

        return len(self.__node_values__.keys())

    @property
    def edge_count(self) -> int:
        """
        Returns the number of edges in the graph.

        Returns:
            int: Count of edges.
        """

        count = 0

        for item in self.__vertex_index__:
            count = count + len(self.__vertex_index__.get(item, set()))
        return count

    def get_relationships(self, canonical_id: str) -> list:
        """
        Returns a Set of Related Nodes for a canonical node value.

        Args:
            canonical_id (str): canonical id for a node

        Returns:
            set: Set of related node canonical ids
        """

        if canonical_id in self.__vertex_index__:
            return list(self.__vertex_index__[canonical_id])

        raise MissingNodeError('Node is not present in the graph.')

    def get_node(self, canonical_id: str):
        """
        Returns the Node value for a given canonical id.

        Args:
            canonical_id (str): Canonical id

        Returns:
            any: Node Value from the Graph.
        """

        if canonical_id in self.__node_values__:
            return self.__node_values__.get(canonical_id)
        raise MissingNodeError('Node not present in the graph.')
