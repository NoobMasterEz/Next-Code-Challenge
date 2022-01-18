
# Next-Code-Challenge
I use Dijkstra's shortest path algorithm  is a greedy algorithm is an iterative algorithm that provides us with the shortest path from one particular starting node  to all other nodes in the graph

- Vertex A vertex is the most basic part of a graph and it is also called a node. Throughout we'll call it note. A vertex may also have additional information and we'll call it as payload.
- Edge An edge is another basic part of a graph, and it connects two vertices/ Edges may be one-way or two-way. If the edges in a graph are all one-way, the graph is a directed graph, or a digraph. The picture shown above is not a digraph.
- Weight Edges may be weighted to show that there is a cost to go from one vertex to another. For example in a graph of roads that connect one city to another, the weight on the edge might represent the distance between the two cities or traffic status.

keep track of the total cost from the start node to each destination we will make use of the distance instance variable in the Vertex class. The distance instance variable will contain the current total weight of the smallest weight path from the start to the vertex in question. \n
The algorithm iterates once for every vertex in the graph; however, the order that we iterate over the vertices is controlled by a priority queueHeap queue is a special tree structure in which each parent node is less than or equal to its child node. \n
In python it is implemented using the heapq module. It is very useful is implementing priority queues where the queue item with higher weight is given more priority in processing


# Result unittest
![Screenshot](Capture.PNG)
