import numpy as np
import graphviz

def createDotGraph(Wpt,Wtp):
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

def renderDotGraph(Wpt,Wtp):
    dot = createDotGraph(Wpt,Wtp)
    dot.render(directory='digraph-output', view=False) 