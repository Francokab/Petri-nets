import numpy as np
import graphviz
from petriNetsClasses import PetriNet
from node import Node

def create_dot_graph_petrinet(PT: PetriNet):
    Wpt = PT.Wpt
    Wtp = PT.Wtp

    def pstr(i):
        return 'p' + str(i)
    def tstr(i):
        return 't' + str(i)
    
    dot = graphviz.Digraph(comment='Graph')
    Np,Nt = Wpt.shape
    for i in range(Np):
        dot.node(pstr(i))
    for i in range(Nt):
        dot.node(tstr(i),shape = 'box')

    for p in range(Np):
        for t in range(Nt):
            if Wpt[p,t] != 0:
                if Wpt[p,t] != 1:
                    dot.edge(pstr(p),tstr(t), label=str(Wpt[p,t]))
                else:
                    dot.edge(pstr(p),tstr(t))
            if Wtp[t,p] != 0:
                if Wtp[t,p] != 1:
                    dot.edge(tstr(t),pstr(p), label=str(Wtp[t,p]))
                else:
                    dot.edge(tstr(t),pstr(p))

    return dot

def create_dot_graph_tree(tree: Node):
    dot = graphviz.Digraph(comment='Graph')
    unprocessed : list[Node] = [tree]
    dot.node(str(tree))
    
    def pstr(i):
        return 'p' + str(i)
    def tstr(i):
        return 't' + str(i)
    
    while (unprocessed != []):
        node = unprocessed[0]
        for transition, new_node in node.transitions.items():
            unprocessed.append(new_node)
            dot.node(str(new_node))
            dot.edge(str(node),str(new_node),label=tstr(transition))
        unprocessed.remove(node)
    return dot

def render_dot_graph(dot):
    dot.render(directory='digraph-output', view=False) 