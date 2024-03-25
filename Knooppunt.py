# Module gebruikt om knooppunten te definiëren
# iedere instance van deze class is een object met de volgende parameters:
# - een positie in het vlak
# - een kracht die inwerkt op dit punt
# - een index/naam van het punt

import numpy as np
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
    def change_index(self,index):
        self.m_graph_index :int = index
        return

    def test_print(self):
        print("Graph index", self.m_graph_index)
        print("position:", self.m_position)
        print("force: ", self.m_force)
        return
