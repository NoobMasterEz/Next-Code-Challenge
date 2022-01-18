
import sys
import unittest
class Vertex_node():
    """
    A vertex is the most basic part of a graph and it is also called a node.
    Throughout we'll call it note. 
    A vertex may also have additional information and we'll call it as payload.
    """

    def __init__(self,Node) -> None:
        self._node = Node
        self._adjacent = {}
        # Set distance to infinity 
        self._distance =  sys.maxsize
        # Mark all nodes unvisited 
        self._visited = False
        self._previous = None

    def __lt__(self,other):
        return self.get_distance < other.get_distance

    def add_neighbor_node(self,key,weight)->None:
        """
        this fucntion add node and weigth .

        Node <--Weight--> neighbor
        
        parameter : 
            key: this from input csv node number type of int  .
            weight: distand between node and neighbor .
    
        """
        
        self._adjacent[key] = weight

    def set_previous(self,prev)->None:
        self._previous = prev

    def set_distance(self,dist)->None:
        self._distance = dist 
    
    def get_weight(self,key):
        return self._adjacent[key]

    @property
    def get_visited(self):
        return self._visited
    
    @property
    def get_previous(self):
        return self._previous
    
    @property    
    def set_visited(self)->None:
        """
        Set status visited True .
        """
        self._visited = True

    @property
    def get_node(self)->str:
        # Return Node id
        return self._node

    @property
    def get_distance(self):
        # Return distance
        return self._distance

    @property
    def get_connected(self):
    
        # Return Node is connected 
    
        return self._adjacent.keys()

    @property
    def get_adjacent(self):
        return self._adjacent

    def __str__(self) -> str:
        return str(self._node) + ' adjacent: ' + str([x.get_node for x in self._adjacent])

