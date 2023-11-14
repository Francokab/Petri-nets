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
    np,nt = Wpt.shape
    for i in range(np):
        dot.node(pstr(i))
    for i in range(nt):
        dot.node(tstr(i),shape = 'box')

    for p in range(np):
        for t in range(nt):
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