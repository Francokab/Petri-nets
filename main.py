import numpy as np
from node import Node
from petriNetsClasses import PetriNet
from dotGraphRenderer import create_dot_graph_petrinet, create_dot_graph_tree, create_dot_graph_tree_with_id, render_dot_graph


def createPT1():
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
                  [-1, -1, -1, -1],
                  [-1, -1, -1, -1],
                  [-1, -1, -1, -1],
                  [-1, -1, -1, -1]],dtype=int)
    
    PT = PetriNet(Wpt,Wtp,M0, I)
    
    return PT

def createPT2():
    Wpt = np.array([[0, 0, 2, 0],
                    [0, 0, 0, 1],
                    [0, 0, 0, 0],],dtype=int)
    
    Wtp = np.array([[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 1],
                    [1, 0, 0],],dtype=int)
    
    M0 = np.array([0,7,0])
    
    I = np.array([[0, 5, -1, -1],
                  [-1, -1, -1, -1],
                  [-1, -1, -1, -1],],dtype=int)
    

    PT = PetriNet(Wpt,Wtp,M0, I)
    return PT

def main():

    PTI = createPT2()
    render_dot_graph(create_dot_graph_petrinet(PTI), "Petri_Net_inhib")
    PT = PTI.PTI_to_PT(6)
    render_dot_graph(create_dot_graph_petrinet(PT), "Petri_Net")
    
    tree = PT.construct_CT_with_bounds(0, PTI)
    render_dot_graph(create_dot_graph_tree_with_id(tree), "Converability_Tree")
    
    # tree = PT.construct_CT()
    # render_dot_graph(create_dot_graph_petrinet(PT), "Petri_Net")
    # render_dot_graph(create_dot_graph_tree_with_id(tree), "Converability_Tree")

if __name__ == "__main__":
    main()

