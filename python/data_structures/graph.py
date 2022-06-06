from data_structures.queue import Queue

class Graph:
    """
    Put docstring here
    """
    def __init__(self, type_of='directed'):
        self._adjacency_list = {}
        self.type = type_of

    def add_node(self, value):
        vertex = Vertex(value)
        if vertex not in self._adjacency_list:
            self._adjacency_list[vertex] = []
            return vertex
        raise Exception('Node already exists in dictionary')

    def get_nodes(self):
        return list(self._adjacency_list.keys())

    def size(self):
        return len(self._adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list or end_vertex not in self._adjacency_list:
            raise KeyError("Either Start or End Vertex not found in Graph")
        edge = Edge(end_vertex, weight)
        self._adjacency_list[start_vertex].append(edge)

        if self.type == 'bidirectional':
            edge = Edge(start_vertex,weight)
            self._adjacency_list[end_vertex].append(edge)


    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

    def breadth_first(self, vertex):
        nodes = []
        breadth = Queue()
        visited = set()

        breadth.enqueue(vertex)
        visited.add(vertex)
        print(visited)

        while breadth.is_empty() is False:
            front = breadth.dequeue()
            print(front)
            nodes.append(front.value)
            print(nodes)

            for neighbor in self.get_neighbors(front):
                if neighbor.vertex not in visited:
                    print(neighbor.vertex)
                    visited.add(neighbor.vertex)
                    breadth.enqueue(neighbor.vertex)
        return nodes


class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
