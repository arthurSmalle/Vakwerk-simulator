adj_list = {}
mylist = []


def add_node(node):
    if node not in mylist:
        mylist.append(node)
    else:
        print("Node ", node, " already exists!")


def add_edge(node1, node2, weight):
    temp = []
    if node1 in mylist and node2 in mylist:
        if node1 not in adj_list:
            temp.append([node2, weight])
            adj_list[node1] = temp

        elif node1 in adj_list:
            temp.extend(adj_list[node1])
            temp.append([node2, weight])
            adj_list[node1] = temp

    else:
        print("Nodes don't exist!")


def graph():
    for node in adj_list:
        print(node, " ---> ", [i for i in adj_list[node]])