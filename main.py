import numpy as np
from dotGraphRenderer import renderDotGraph
from petriNetsClasses import PetriNet



def main():
    Wpt = np.array([[1, 0, 0, 0],
                    [1, 0, 1, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 1],
                    [0, 0, 0, 1],
                    [0, 0, 0, 0],],dtype=int)

    Wtp = np.array([[0, 1, 1, 1, 0, 0],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 1],],dtype=int)

    M0 = np.array([1, 1, 0, 0, 0, 0])

    PT = PetriNet(Wpt,Wtp,M0)

    renderDotGraph(PT)

if __name__ == "__main__":
    main()

