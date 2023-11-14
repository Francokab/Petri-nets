import numpy as np
from dotGraphRenderer import renderDotGraph
from petriNetsClasses import PetriNet

def construct_CT(PT: PetriNet):
    pass
    # Initialize tree
    # Initialize unprocessed
    # while unprocessed is not null
        # select an element M1 of unprocessed
        # if the element is not already a processed element of the tree
            # for each possible transition from this element
                # add the new element (M2) to the tree and to unprocessed
                # if there is a path between M3 -> M1 with M3 < M2
                    # if M3[p] < M2[i] then M2[i] = inf
            # remove the element M1 from unprocessed
    # return the tree

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

