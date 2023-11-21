import numpy as np
from node import Node
from petriNetsClasses import PetriNet
from dotGraphRenderer import create_dot_graph_petrinet, create_dot_graph_tree, render_dot_graph, renderDotGraph


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
    render_dot_graph(create_dot_graph_petrinet(PT))
    tree = PT.construct_CT()

if __name__ == "__main__":
    main()

