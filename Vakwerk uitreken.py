import numpy as np


class Graph:
    # Constructor
    def __init__(self, num_of_nodes , directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed

    # Different representations of a graph
        self.m_list_of_edges = []


    # Add edge to a graph
    def add_edge(self, node1, node2, weight=1):
        # Add the edge from node1 to node2
        self.m_list_of_edges.append([node1, node2, weight])

        # If a graph is undirected, add the same edge,
        # but also in the opposite direction
        if not self.m_directed:
          self.m_list_of_edges.append([node1, node2, weight])

    # Print a graph representation
    def print_edge_list(self):
        num_of_edges = len(self.m_list_of_edges)
        for i in range(num_of_edges):
            print("edge ", i + 1, ": ", self.m_list_of_edges[i])

def solveSystem(F1 = 0 , F2 = 0, S1 = 0, S2 = 0, F3 = None, S3 = 0, F4 = None, S4 = 0):
    if F3 == None:
        print("2 delig stelsel")
        # define left-hand side of equation
        left_side = np.array([F1,F2])

        # define right-hand side of equation
        right_side = np.array([S1,S2])

        # solve for x and y
        oplossing = np.linalg.inv(left_side).dot(right_side)
    elif F4 == None:
        print("3 delig stelsel")
        # define left-hand side of equation
        left_side = np.array([F1, F2, F3])

        # define right-hand side of equation
        right_side = np.array([S1, S2, S3])

        # solve for x and y
        oplossing = np.linalg.inv(left_side).dot(right_side)
    else:
        print("4 delig stelsel")
        # define left-hand side of equation
        left_side = np.array([F1, F2, F3, F4])

        # define right-hand side of equation
        right_side = np.array([S1, S2, S3, S4])

        # solve for x and y
        oplossing = np.linalg.inv(left_side).dot(right_side)
    return oplossing
