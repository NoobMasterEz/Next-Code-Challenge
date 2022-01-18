
from lib import Graph
import heapq
import csv
from collections import OrderedDict
from string import digits



def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.get_previous:
        path.append(v.get_previous.get_node)
        shortest(v.get_previous, path)
    return

def dijkstra(aGraph, start):
    """
    Dijkstra's shortest path
    keep track of the total cost from the start node to each destination we will make use of the distance instance variable in the Vertex class. 
    The distance instance variable will contain the current total weight of the smallest weight path from the start to the vertex in question. \n 
    The algorithm iterates once for every vertex in the graph; however, the order that we iterate over the vertices is controlled by a priority queueHeap queue is a special tree structure in which each parent node is less than or equal to its child node.
    In python it is implemented using the heapq module. It is very useful is implementing priority queues where the queue item with higher weight is given more priority in processing

    parameter :
            aGraph: that was created from class Graph .
            start: vertex  that was created from Graph too .

    """
    # Set the distance for the start node to zero
    start.set_distance(0)

    # Transform data in aGraph from to list for heap sort
    to_list= [(i.get_distance,i) for i in aGraph ]
    heapq.heapify(to_list)
    while(len(to_list)):
        # Pops a vertex with the smallest distance
        get_colum = heapq.heappop(to_list)
        current = get_colum[1]
        current.set_visited
        for node in current.get_adjacent:
            if node.get_visited :
                continue

            #print(f"node = {current.get_node} , distance = {current.get_distance}, weight=  {current.get_weight(node)}")
            new_dist = (current.get_distance + current.get_weight(node))
            #print(new_dist , node.get_distance)
            if new_dist < node.get_distance:
                node.set_distance(new_dist)
                node.set_previous(current)
                #print(f"{current.get_node}-->{node.get_node} = {node.get_distance}")
            else:
                #print(f"not up date {current.get_node}-->{node.get_node} = {node.get_distance}")
                pass

        while(len(to_list)):
            heapq.heappop(to_list)

        to_list = [(i.get_distance,i)for i in aGraph if not i.get_visited]
        heapq.heapify(to_list)





def create_head_vertex(reader):
    """
    Tranform csv to string
    """
    all_string = ""
    for i in reader:
        all_string += str(i[0]) + str(i[1])
    return all_string


def builder(file_name,node_start,node_end):
    #defi string 
    all_sort = ""

    # Create graph
    g=Graph.Graph()

    # input filename
    #file_name = input("what is graph file name : ")

    if not(isinstance(file_name,str)) :
        return  
    file = open(file_name,"r")

    #Tranform header
    reader = [i  for i in csv.reader(file, delimiter = ',')]
    Header = ("".join(OrderedDict.fromkeys(create_head_vertex(reader)))).translate(str.maketrans('', '', digits))
    for i in Header:
        # Create Vertex
        g.add_vertex(str(i))

    for i in reader:
        # Add edge
        g.add_edge(str(i[0]), str(i[1]), int(i[2]) )

    #g.show this method show all distance
    #node_start=input("what is start node ?:")
    dijkstra(g,g.get_vertex(node_start))
    #node_end=input("what is gloal node ?:")
    target = g.get_vertex(node_end)
    path = [target.get_node]
    shortest(target,path)

    # print pattern
    for i in range(len(path[::-1])):
        if i+1 != len(path[::-1]) :
            all_sort += "{}->".format(path[::-1][i])
        else:
            all_sort += "{}".format(path[::-1][i])

    print(f"Path from = {all_sort} and have cost {target.get_distance}")
    file.close()
    return target.get_distance
