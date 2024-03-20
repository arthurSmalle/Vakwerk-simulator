class Graph:
    # Constructor
    def __init__(self, num_of_nodes , directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)

        # Define if list is directed
        self.m_directed = directed

    # Different representations of a graph
        self.m_list_of_edges = []
        self.m_adj_list = {node: set() for node in self.m_nodes} #NOTE: make sure to add nodes that are type int in the range of the "num of nodes" (otherwise keyerror)



    # Add edge to a graph
    def add_edge(self, node1, node2, rico=0):
        # Add the edge from node1 to node2
        ## Add for edge list
        self.m_list_of_edges.append([node1, node2, rico])
        ## Add for adj list
        self.m_adj_list[node1].add((node2, rico))

        # If a graph is undirected, add the same edge,
        # but also in the opposite direction
        if not self.m_directed:
        ## Add for edge list
            self.m_list_of_edges.append([node1, node2, rico])
        ## Add for adj list
            self.m_adj_list[node2].add((node1, rico))

    # Print a graph representation
    ## Print edge list
    def print_edge_list(self):
        num_of_edges = len(self.m_list_of_edges)
        for i in range(num_of_edges):
            print("edge ", i + 1, ": ", self.m_list_of_edges[i])
    ## Print adjacency list
    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])