import numpy as np
from Vakwerk import Vakwerk


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

vakwerk1 = Vakwerk()
vakwerk1.print_knooppunten()