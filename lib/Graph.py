from platform import node
from .Vertex import Vertex_node


class Graph():
    def __init__(self) -> None:
        self.vertex_dict = dict()
        self.num_vertices = 0
    
    def __iter__(self):
        """
        function returns an iterator object that goes through each element of the given object.
        """
        return iter(self.vertex_dict.values())

    def __le__(self,other):
        return (self < other) == (self == other)

    def add_vertex(self,node):
        """
        this function add like linked list . \n
            "A" : Vertex_node(A) ...

        parameter : 
            node : data type str

        return : 
            vertex_dict 

        """
        self.num_vertices = self.num_vertices + 1 
        self.vertex_dict[node] = Vertex_node(node)

        return Vertex_node(node)

    def get_vertex(self,node):
        """
        Getter vertex from vertex_dict.
        """
        if node in self.vertex_dict:
            return self.vertex_dict[node]
        else: 
            return None

    def add_edge(self,current,to,cost = 0):
        """
        current , to, cost \n
        Ex   A ,   B ,  0
                   
        parameter : 
            current :Node data type str
            to : Node data type str
            cost : weight data type int 
        """
        if  isinstance(current, str) and isinstance(to, str) :
            pass
        if current not in self.vertex_dict:
            self.add_vertex(current)
        if to not in self.vertex_dict:
            self.add_vertex(to)
 

        self.vertex_dict[current].add_neighbor_node(self.vertex_dict[to],cost)
        self.vertex_dict[to].add_neighbor_node(self.vertex_dict[current],cost)
    
    @property
    def get_vertices(self):
        return self.vertex_dict.keys()

    def set_previous(self,current):
        self.previous = current

    @property
    def get_previous(self):
        return self.previous 

    def __str__(self) -> str:
        return str(self.vertex_dict)

    @property
    def show(self):
        for i in self.vertex_dict: 
            print(f"Node {self.vertex_dict[i]}")
        
        for Node in self.vertex_dict:
            for key in self.vertex_dict[Node].get_connected:
                print(f"{self.vertex_dict[Node].get_node} -> {key.get_node} = {self.vertex_dict[Node].get_weight(key)}")


