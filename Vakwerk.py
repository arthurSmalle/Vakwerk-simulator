from Graph import Graph
from Knooppunt import KnoopPunt
class Vakwerk:
    def __init__(self, extradistance=0, extraKnooppunten= None, Verbindingen = None):
        # lijst met alle knooppunten
        self.m_knooppunten = []
        # Init graph met verbindingen tussen alle knooppunten
        if extraKnooppunten != None:
            self.m_verbindingen = Graph(3 + len(extraKnooppunten), False)
        else:
            self.m_verbindingen = Graph(3,False)


        # basispunten
        steunpunt0 = KnoopPunt(0,0,0,0,0)
        steunpunt1 = KnoopPunt(90 + extradistance * 2,0,0,0,1)
        punthoek = KnoopPunt(45 + extradistance,40,0,0,2)
        self.m_knooppunten.append(steunpunt0)
        self.m_knooppunten.append(steunpunt1)
        self.m_knooppunten.append(punthoek)
        # verbindingen tussen basispunten
        self.m_verbindingen.add_edge(0,1)
        self.m_verbindingen.add_edge(0,2)
        self.m_verbindingen.add_edge(1,2)


        # voeg de extra knooppunten toe aan de lijst
        if extraKnooppunten != None:
            start_index :int = 2  # index vanaf waar de prebuild punten stoppen
            for i in range(len(extraKnooppunten)):
                extraKnooppunten[i].change_index(i + start_index) # change index (index moet veranderd worden zodat het klopt in dit vakwerk)
                self.m_knooppunten.append(extraKnooppunten[i])

    def print_knooppunten(self,index=None):
        if index == None:
            for i in range(len(self.m_knooppunten)):
                print("+---------------------------+")
                self.m_knooppunten[i].test_print()
                print(self.m_verbindingen.m_adj_list[i])
        else:
            self.m_knooppunten[index].test_print()
            print(self.m_verbindingen.m_adj_list[index])
