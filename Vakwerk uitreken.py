import numpy as np


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
    def add_edge(self, node1, node2, weight=1):
        # Add the edge from node1 to node2
        ## Add for edge list
        self.m_list_of_edges.append([node1, node2, weight])
        ## Add for adj list
        self.m_adj_list[node1].add((node2))

        # If a graph is undirected, add the same edge,
        # but also in the opposite direction
        if not self.m_directed:
        ## Add for edge list
            self.m_list_of_edges.append([node1, node2, weight])
        ## Add for adj list
            self.m_adj_list[node2].add((node1))

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


class KnoopPunt:
    # Construction
    def __init__(self, posx, posy, forcex, forcey, graph_index=0 ):
        self.m_position = np.array([posx, posy])  # positie vd vector
        self.m_force = np.array([forcex, forcey])  # krachtvector in het knooppunt
        self.m_graph_index = graph_index  # index zodat het gekoppeld kan worden met de graph
        return

    def add_force(self, forcex, forcey):
        self.m_force += np.array([forcex,forcey])
        return

    def change_position(self,posx,posy):
        validation :str = str(input("Are you sure you want to change position?\ny/n\n"))
        if validation == "y":
            self.m_position = np.array([posx,posy])
        else:
            print("Position change aborted")
            return
        return

    def test_print(self):
        print("Graph index", self.m_graph_index)
        print("position:", self.m_position)
        print("force: ", self.m_force)
        return


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
def  maximumHoekVDTopHoek(dist=0): # dist is de extra lengte die verkregen wordt door een wat groter gat dan 90cm te maken
    steun_hoek = np.arctan(40/(45+dist)) # de hoek tussen de balk en de tafel
    print("steun hoek:", np.rad2deg(steun_hoek), "degrees")
    top_hoek =  np.pi - (2 * steun_hoek)
    print("top hoek", np.rad2deg(top_hoek), "degrees")
    return top_hoek