########################################
# PROJECT 8 - Graph
# Author: Sayem Lincoln
# PID: A54207835
########################################
import random
import copy


class Edge(object):
    def __init__(self, source, destination, weight):
        """
        DO NOT EDIT!
        Class representing an Edge in a graph
        :param source: Vertex where this edge originates
        :param destination: Vertex where this edge ends
        :param weight: Value associated with this edge
        """
        self.source = source
        self.destination = destination
        self.weight = weight

    def __eq__(self, other):
        return self.source == other.source and self.destination == other.destination

    def __repr__(self):
        return f"Source: {self.source} Destination: {self.destination} Weight: {self.weight}"

    __str__ = __repr__


class Path(object):
    def __init__(self, vertices=list(), weight=0):
        """
        DO NOT EDIT!
        Class representing a path in a graph
        :param vertices: Ordered list of vertices that compose the path
        :param weight: Total weight of the path
        """
        self.vertices = vertices
        self.weight = weight

    def __eq__(self, other):
        return self.vertices == other.vertices and self.weight == other.weight

    def __repr__(self):
        return f"Weight:{self.weight} Path: {' -> '.join([str(v) for v in self.vertices])}\n"

    __str__ = __repr__

    def add_vertex(self, vertex):
        """
        Add a vertex id to the path
        :param vertex: id of a vertex
        :return: None
        """
        self.vertices.append(vertex)

    def add_weight(self, weight):
        """
        Add weight to the path
        :param weight: weight
        :return: None
            """
        self.weight += weight

    def remove_vertex(self):
        """
        Remove the most recently added vertex from the path
        :return: None
        """
        if not self.is_empty():
            self.vertices.pop()

    def is_empty(self):
        """
        Check if the path object is empty
        :return: True if empty, False otherwise
        """
        return len(self.vertices) == 0


class Vertex(object):
    def __init__(self, number):
        """
        Class representing a vertex in the graph
        :param number: Unique id of this vertex
        """
        self.edges = []
        self.id = number
        self.visited = False

    def __repr__(self):
        return f"Vertex: {self.id}"

    __str__ = __repr__

    def add_edge(self, destination, weight):
        edge = Edge(self, destination, weight)
        self.edges.append(edge)

    def degree(self):
        return len(self.edges)

    def get_edge(self, destination):
        for edge in self.edges:
            if edge.destination == destination:
                return edge

        return None

    def get_edges(self):
        return self.edges


class Graph(object):
    def generate_edges(self):
        """
        DO NOT EDIT THIS METHOD
        Generates directed edges between vertices to form a DAG
        :return: List of edges
        """
        random.seed(10)
        edges = []
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if random.randrange(0, 100) <= self.connectedness * 100:
                    edges.append([i, j, random.randint(-10, 50)])
        return edges

    def __init__(self, size=0, connectedness=0):
        """
        DO NOT EDIT THIS METHOD
        Construct a random DAG
        :param size: Number of vertices
        :param connectedness: Value from 0 - 1 with 1 being a fully connected graph
        """
        assert connectedness <= 1
        self.adj_map = {}
        self.size = size
        self.connectedness = connectedness
        self.construct_graph()

    def construct_graph(self):
        """
        Adds all edges created in generate_edges to the graph. generate_edges will return
        a list of lists containing edges in this format: [source, destination, weight]
        :param : Uses the dictionary self.adj_map to store vertices’ IDs as keys and their objects as
                values.
        :return: None
        """
        ge = self.generate_edges()
        list_vertices = []
        for i in range(self.size): 
            list_vertices.append(Vertex(i))

        for i in range(self.size):
            for item in ge:
                if list_vertices[i].id == item[0]:
                    list_vertices[i].add_edge(list_vertices[item[1]], item[2])

        for i in range(self.size):
            self.adj_map[list_vertices[i].id] = list_vertices[i]   

    def vertex_count(self):
        """
        :param : run in O(1) time
        :return: the number of vertices in the graph.
        """
        return self.size

    def vertices(self):
        """
        :param : run in O(V) time
        :return: a list of all Vertex objects in the graph.
        """
        list_vertices = []
        for key in self.adj_map.keys():
            list_vertices.append(self.adj_map[key])
        return list_vertices

    def insert_edge(self, source, destination, weight):
        """
        Inserts a new Edge from source to destination with a specified weight. If the edge
        is already in the graph, replace the weight.
        :param : run in O(source’s degree) time
        :return: None.
        """
        for edge in self.adj_map[source.id].edges:
            if edge.destination == destination:
                edge.weight = weight
                return
        source.add_edge(destination, weight)

    def find_valid_paths(self, source, destination, limit):
        """
        Finds all valid paths between two vertices in the graph. A path is valid if the total
        accrued weight along the path does not exceed the limit. Store those valid paths
        as Path objects.
        Path objects contain an ordered list of visited vertices and the total weight along
        the path
        :param : Worst case time complexity: O((V-1)!)
        :return: python list[Path]
        """
        def find_simple_paths(graph, start, end):
            #function for fining simple path from start to end
            set_visited = set()
            set_visited.add(start)

            list_nodes = list()
            list_indexes = list()
            item = start
            i = 0

            while True:
                #loop for checking neighbors
                neighbors = graph[item]

                while i < len(neighbors) and neighbors[i] in set_visited:
                    i += 1

                if i >= len(neighbors):
                    set_visited.remove(item)
                    if len(list_nodes) < 1:
                        break 
                    item = list_nodes.pop()
                    i = list_indexes.pop()
                elif neighbors[i] == end:
                    yield list_nodes + [item, end]
                    i += 1
                else:
                    list_nodes.append(item)
                    list_indexes.append(i+1)
                    set_visited.add(neighbors[i])
                    item = neighbors[i]
                    i = 0
        graph = {}
        for key in self.adj_map.keys():
            graph[key] = [edge.destination.id for edge in self.adj_map[key].edges]

        list_paths = []
        for item in find_simple_paths(graph,source, destination):
            weight = 0
            i = 0
            while i < len(item) - 1:
                #for finding edge destination
                for edge in self.adj_map[item[i]].edges:
                    if edge.destination == self.adj_map[item[i + 1]]:
                        weight += edge.weight
                i += 1
                
            path = Path([self.adj_map[v] for v in item], weight)

            if weight <= limit:
                list_paths.append(path)
        return list_paths       

    def find_shortest_path(self, source, destination, limit):
        """
        Return a valid Path with the smallest total weight. If there are multiple paths,
        return any one.
        :param : Worst case time complexity: O((V-1)!)
        :return:Path
        """
        list_paths = self.find_valid_paths(source, destination, limit) 
        shortest_path = list_paths[0]
        #finding path in list
        for path in list_paths:
            if shortest_path.weight > path.weight:
                shortest_path = path

        return shortest_path

    def find_longest_path(self, source, destination, limit):
        """
        Return a valid Path with the largest total weight. If there are multiple paths,
        return any one.
        :param : Worst case time complexity: O((V-1)!)
        :return:Path
        """
        list_paths = self.find_valid_paths(source, destination, limit) 
        shortest_path = list_paths[0]
        #finding path in list
        for path in list_paths:
            if shortest_path.weight < path.weight:
                shortest_path = path

        return shortest_path

    def find_most_vertices_path(self, source, destination, limit):
        """
        Return a valid Path that visits the most vertices. If there are multiple paths, return
        any one..
        :param : Worst case time complexity: O((V-1)!)
        :return:Path
        """
        list_paths = self.find_valid_paths(source, destination, limit) 
        shortest_path = list_paths[0]
        #finding path in list
        for path in list_paths:
            if len(shortest_path.vertices) < len(path.vertices):
                shortest_path = path

        return shortest_path

    def find_least_vertices_path(self, source, destination, limit):
        """
        Return a valid Path that visits the least vertices. If there are multiple paths, return
        any one..
        :param : Worst case time complexity: O((V-1)!)
        :return:Path
        """
        list_paths = self.find_valid_paths(source, destination, limit) 
        shortest_path = list_paths[0]
        #finding path in list
        for path in list_paths:
            if len(shortest_path.vertices) > len(path.vertices):
                shortest_path = path

        return shortest_path
