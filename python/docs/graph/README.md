# Graphs


## Challenge
Implement your own graph, it should be represented as an adjacency list.

## Approach & Efficiency

Most functionality of this Datastructure is Time O(1) - it wll always take the same amount of time to run each method regardless of what you are doing.

Space: This datastructure takes an O(n) space, due to the fact that it takes up more space as nodes/vertexes are added.

## API
`add_node` - Adds a node to the graph

`add_edge` - adds an edge (takes in two nodes and weight(optional))

`get_nodes` - returns all nodes in a graph

`get neighbors` - returns a collection of edges connected to given node.

`size`  returns total number of nodes in graph