import numpy as np
from node import node

# P set of place : int from 0 to n-1
# T set of transition : int from 0 to m-1
# W represent the number of token that move in a transition
    # Wpt matrix n*m int p->t represent the decrement of places during the transition
    # Wtp matrix m*n int t->p represent the increment of places during the transition
# M0 et M represent the states of the places : array of int of size n
# I represent the inhibition of places on transition
# I matrix n*m int, if p>I(p,t) then t can't happen
# negative value are infinite


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

