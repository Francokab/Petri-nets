import numpy as np
import graphviz
from petriNetsClasses import PetriNet

def createDotGraph(PT: PetriNet):
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

def renderDotGraph(PT: PetriNet):
    dot = createDotGraph(PT)
    dot.render(directory='digraph-output', view=False) 