import numpy as np
from node import Node
from petriNetsClasses import PetriNet
from dotGraphRenderer import create_dot_graph_petrinet, create_dot_graph_tree, create_dot_graph_tree_with_id, render_dot_graph


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
    
    I = np.array([[0, 5, -1, -1],
                  [-1, -1, -1, -1],
                  [-1, -1, -1, -1],],dtype=int)

    PT = PetriNet(Wpt,Wtp,M0, None)

    PT.PTI_to_PT()

    tree = PT.construct_CT()
    render_dot_graph(create_dot_graph_petrinet(PT), "Petri_Net")
    render_dot_graph(create_dot_graph_tree_with_id(tree), "Converability_Tree")

if __name__ == "__main__":
    main()

